# 部署

## 环境要求

| 项 | 要求 |
|---|---|
| Docker | 20.10+ |
| 架构 | `linux/amd64`（ARM 见下方"自行构建"） |
| 内存 | 建议 1 GB 以上 |
| 磁盘 | 镜像 1.1 GB + 数据（按媒体库规模） |

## 方式一：镜像 + compose（推荐）

```bash
# 1. 下载
wget https://github.com/xhdyycx/media-cms/releases/download/v1.0/novamedia-v1.0.tar
wget https://github.com/xhdyycx/media-cms/releases/download/v1.0/SHA256SUMS.txt

# 2. 校验（务必做）
sha256sum -c SHA256SUMS.txt

# 3. 导入
docker load -i novamedia-v1.0.tar
# 输出: Loaded image: novamedia:v1.0

# 4. 起容器
git clone https://github.com/xhdyycx/media-cms.git
cd media-cms
cp .env.example .env
vim .env
docker compose up -d

# 5. 看日志
docker compose logs -f
```

正常启动的关键日志：

```
Version: v0.5.0.3
Uvicorn running on http://0.0.0.0:9528
```

`nginx` 不会打日志到 stdout，nginx 的日志在 `./logs/nginx/`。

## 方式二：纯 docker run

不想用 compose：

```bash
mkdir -p ./config ./logs

docker run -d \
  --name media-cms \
  --restart unless-stopped \
  -p 9527:9527 -p 9096:9096 \
  -e TZ=Asia/Shanghai \
  -e PUID=1000 -e PGID=1000 \
  -e EMBY_HOST_PORT=http://172.17.0.1:8096 \
  -e EMBY_API_KEY=你的key \
  -v $(pwd)/config:/config \
  -v $(pwd)/logs:/logs \
  novamedia:v1.0
```

## 方式三：从源码跑（不用容器）

适合调试后端。需要 Python 3.12：

```bash
cd src/cms-api
python -m venv .venv && source .venv/bin/activate
pip install blacksheep uvicorn guardpost requests pyjwt aiohttp \
            pillow qrcode urllib3 cryptography

export PYTHONPATH=.
export HOME=$PWD/..
export RUN_ENV=online
python app/main.py
```

此时后端直接监听 `9528`，前端静态文件需要另起一个 nginx 或用 `python -m http.server` 指到 `src/web`。

**注意**：源码运行缺少容器内的 `constant.js` 模板渲染，Emby 反代功能不完整。仅建议用于阅读代码和调试 API。

## 反向代理 / HTTPS

面板默认走 HTTP。要挂 HTTPS，在前面加一层：

**Caddy**

```caddyfile
media.example.com {
    reverse_proxy 127.0.0.1:9527
}
```

**Nginx**

```nginx
server {
    listen 443 ssl http2;
    server_name media.example.com;

    ssl_certificate     /etc/ssl/fullchain.pem;
    ssl_certificate_key /etc/ssl/privkey.pem;

    client_max_body_size 100m;

    location / {
        proxy_pass http://127.0.0.1:9527;
        proxy_set_header Host              $host;
        proxy_set_header X-Real-IP         $remote_addr;
        proxy_set_header X-Forwarded-For   $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_read_timeout 300s;
    }
}
```

**播放端口也要一起反代**，否则外网访问时 Emby 还是去拉内网 `:9096`：

```nginx
server {
    listen 443 ssl http2;
    server_name play.example.com;

    location / {
        proxy_pass http://127.0.0.1:9096;
        proxy_http_version 1.1;
        proxy_set_header Range $http_range;          # 拖动进度条必须
        proxy_set_header If-Range $http_if_range;
        proxy_buffering off;                          # 边下边播，不要缓冲
        proxy_read_timeout 3600s;
    }
}
```

## 自行构建（ARM NAS）

镜像只有 `amd64`。ARM 机器（群晖 ARM 型号、树莓派）需要自己构建：

```bash
docker buildx build --platform linux/arm64 -t novamedia:v1.0-arm64 .
```

需要 Dockerfile —— 当前仓库未附带，可按 `docs/architecture.md` 里的进程模型自己写：Debian 12 + Python 3.12 + nginx + 上述 `src/` 目录结构。

## 升级

```bash
docker compose down
docker load -i novamedia-v1.1.tar
docker compose up -d
```

`./config` 不动，数据自动沿用。**升级前先备份 `config` 目录**。

## 卸载

```bash
docker compose down
# 数据还在 ./config，确认不要了再删
rm -rf ./config ./logs
docker rmi novamedia:v1.0
```

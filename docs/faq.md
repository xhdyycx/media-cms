# 常见问题

## 启动

### 容器起来了但面板打不开

先看后端有没有真正起来：

```bash
docker logs media-cms --tail 50
```

正常应该看到 `Uvicorn running on http://0.0.0.0:9528`。

看不到就是后端挂了，往下看 `Traceback`。

**如果后端正常但仍打不开**：检查宿主机端口有没有被占。

```bash
ss -lntp | grep -E '9527|9096'
```

### 端口 9527 被占用

改 compose 的映射，比如 `19527:9527`，但**内部端口不能改**（nginx 写死了）。

### 一直 `Restarting`

看 `docker logs`。最常见的三个原因：

| 日志 | 原因 |
|---|---|
| `PermissionError: /config` | `PUID`/`PGID` 与目录属主不匹配，`chown -R 1000:1000 ./config` |
| `Address already in use` | 上次容器没清干净，`docker rm -f media-cms` |
| `sqlite3.OperationalError: unable to open database file` | `./config` 目录不存在或不可写 |

### 首次启动很慢（20 秒以上）

正常。启动时要建库、跑初始化 SQL、加载调度器。40 秒内起来都算正常。

## Emby

### Emby 扫不到媒体

三件事按顺序查：

1. **STRM 有没有生成** — 进容器看输出目录：`docker exec media-cms ls /config/../media` 或者你配的路径
2. **Emby 能不能读到那个目录** — Emby 容器必须挂载同一个路径
3. **STRM 里的地址对不对** — `cat xxx.strm`，应该是一个 `http://...:9096/d/...` 的地址

### 点播放转圈 / 403

```bash
# 在宿主机上直接打这个地址
curl -I "http://127.0.0.1:9096/d/<file_id>"
```

| 返回 | 原因 |
|---|---|
| `403` | 网盘登录态失效，面板里重新授权 |
| `404` | 文件 ID 失效，该资源已被删或移动 |
| `502` | 后端没起来 |
| 一直挂着不回 | 网盘接口慢或网络不通，看 `./logs` |

### 拖动进度条从头开始

反代的 `Range` 头被吃掉了。如果你在前面加了 nginx，必须显式透传：

```nginx
proxy_set_header Range $http_range;
proxy_set_header If-Range $http_if_range;
proxy_buffering off;
```

直连 `:9096` 不会有这个问题。

## 网盘

### 115 老是掉线

115 的登录态会过期。三种方式稳定性递增：

1. 账号密码 —— 最不稳，异地登录就掉
2. Cookie —— 中等，手动从浏览器复制
3. 开放平台应用 —— 最稳，需要申请

面板 → 设置 → 115 里能看到当前用的是哪种。

### AList 连不上

`alistAddr` 默认是 `http://172.17.0.1:5244`（宿主机上的 AList）。如果 AList 在别的机器，改成实际地址。

测一下容器能不能通：

```bash
docker exec media-cms curl -I http://172.17.0.1:5244
```

## 数据

### 忘了面板密码

```bash
docker exec -it media-cms sqlite3 /config/cms-online.db \
  "UPDATE user SET password='<新密码的哈希>' WHERE username='admin';"
```

密码是 bcrypt 哈希，不能直接写明文。更省事的办法：删掉 `config/cms-online.db` 里的 `user` 表数据，重启后会用默认 `admin/admin` 重建。

### 迁移到新机器

```bash
# 旧机器
docker compose down
tar czf cms-config.tar.gz config/

# 新机器
tar xzf cms-config.tar.gz
docker compose up -d
```

`logs/` 不用带。

### 数据库多大算正常

空库约 200 KB。10 万条媒体索引大约 300 MB。超过 1 GB 说明索引没清理，面板里跑一次"清理失效记录"。

### 能同时跑两个实例吗

不能共用一个 `config`。SQLite 没有跨进程写锁协调，两个容器写同一个库会损坏。

要跑多实例，各自独立 `config`，前面用 nginx 做负载均衡没有意义 —— 它们的任务调度会互相打架。

## 其他

### 支持 ARM 吗

官方镜像只有 `amd64`。ARM 需要自己构建，见 [deployment.md](deployment.md#自行构建arm-nas)。

### 支持 Windows 吗

Docker Desktop 可以跑（WSL2 后端）。注意 `EMBY_HOST_PORT` 要填 `http://host.docker.internal:8096`。

### 会不会往外面传数据

后端出网只有三个方向：网盘 API、TMDB API、以及网盘资源本身。没有遥测、没有回传。

验证方法：

```bash
docker exec media-cms cat /proc/net/tcp | awk 'NR>1 {print $3}'
```

看有没有指向陌生地址的长连接。

### 日志在哪

| 内容 | 位置 |
|---|---|
| 应用日志 | `./logs/` |
| nginx 访问/错误 | `./logs/nginx/` |
| 容器 stdout | `docker logs media-cms` |
| 任务执行记录 | 面板 → 任务 → 历史 |

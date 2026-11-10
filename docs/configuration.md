# 配置

## 环境变量

镜像内置的默认值，`docker run -e` 或 `.env` 覆盖。

| 变量 | 默认 | 说明 |
|---|---|---|
| `TZ` | `Asia/Shanghai` | 时区。影响定时任务触发时间与日志时间戳 |
| `PUID` | `0` | 生成文件的 UID。NAS 上改成你的用户 ID（`id -u`） |
| `PGID` | `0` | 生成文件的 GID（`id -g`） |
| `UMASK` | `022` | 文件权限掩码 |
| `RUN_ENV` | `online` | 运行环境标识 |
| `EMBY_HOST_PORT` | `http://172.17.0.1:8096` | 容器视角的 Emby 地址 |
| `EMBY_API_KEY` | 空 | Emby API Key |
| `EMBY_LOCAL_FILE_PATH` | 空 | 宿主机本地媒体路径，逗号分隔。留空则全走 HTTP |
| `IMAGE_CACHE_POLICY` | `3` | 封面缓存：0 关 / 1 内存 / 2 磁盘 / 3 磁盘+LRU |
| `EMBY_PROXY_PORT` | `9096` | Emby 反代监听端口。**改这里要同步改 `ports`** |
| `CMS_API_TOKEN` | `cloud_media_sync` | 内部 API 令牌，一般不用改 |
| `HOME` | `/cms` | 应用根目录，改动会导致找不到静态资源 |
| `PYTHONPATH` | `/cms/cms-api` | 决定哪份代码被加载，**不要改** |

### EMBY_HOST_PORT 怎么填

容器里访问宿主机上的 Emby，三种网络方式对应三种地址：

| Emby 部署方式 | 填什么 |
|---|---|
| Emby 在同宿主机，Docker 默认网桥 | `http://172.17.0.1:8096` |
| Emby 在同宿主机，Docker Desktop | `http://host.docker.internal:8096` |
| Emby 在另一台机器 | `http://192.168.x.x:8096` |
| 本容器用 host 网络 | `http://127.0.0.1:8096` |

填错的表现：面板能开，但"测试连接"一直失败。

### EMBY_LOCAL_FILE_PATH 什么时候需要

默认模式是**纯 HTTP 代理**：Emby 请求 `:9096`，后端去网盘取流。这条链路不落盘，但每次播放都要经过一次转发。

如果你的网盘已经通过 rclone / clouddrive 挂载到宿主机，可以让 Emby 直接读本地文件，跳过代理：

```yaml
volumes:
  - /mnt/cloud:/media:ro
environment:
  - EMBY_LOCAL_FILE_PATH=/mnt/cloud
```

生成的 STRM 会指向本地路径，播放速度取决于挂载方式。

## 面板里的配置

环境变量只管系统级参数，业务配置在面板里：

| 位置 | 配什么 |
|---|---|
| 设置 → 115 | 账号密码 / Cookie / 开放平台应用 |
| 设置 → 阿里云盘 | Token 或扫码授权 |
| 设置 → 123 云盘 | 账号密码 |
| 设置 → AList | 服务地址 + Token |
| 设置 → Emby | 地址、API Key、媒体库路径 |
| 设置 → TMDB | API Key（可留空用内置） |
| 设置 → 路径 | STRM 输出目录、重命名规则 |
| 任务 | 各定时任务的 cron 与开关 |

面板配置全部存进 `config/cms-online.db`，不进环境变量。

## 定时任务

默认任务（可在面板改 cron 或关掉）：

| 任务 | 默认频率 | 做什么 |
|---|---|---|
| 媒体同步 | 每小时 | 扫描网盘新增，生成 STRM |
| 元数据刮削 | 每天 | 查 TMDB，写 nfo |
| 封面生成 | 按需 | 为缺封面的条目合成海报 |
| 115 签到 | 每天 | 保活 |
| 回收站清理 | 每周 | 清网盘回收站 |
| 缓存刷新 | 每 6 小时 | 清理过期封面缓存 |

时间按 `TZ` 计算，不是 UTC。

## 配置导入导出

面板 → 设置 → 备份：

- **导出**：把当前配置序列化成 JSON（不含网盘登录态）
- **导入**：覆盖现有配置

网盘 Cookie / Token 不在导出范围内，换机器后要重新授权。

## 数据库直连

SQLite，随便找个客户端就能改：

```bash
docker exec -it media-cms sqlite3 /config/cms-online.db
.tables
```

**改动前先 `cp cms-online.db cms-online.db.manual-bak`** —— 面板和后端同时持有连接，写坏了自己负责。

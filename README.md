# Media CMS

自托管的媒体库协同管理系统。把网盘里的资源变成 Emby 能直接播放的媒体库。

> **English** — A self-hosted media library sync and management system. It bridges cloud drives (115 / Aliyun / 123 / AList) to an Emby server: generates STRM files, proxies playback, scrapes metadata, and keeps everything on a schedule.

---

## 这是什么

你在网盘里存了几 TB 的片子，但 Emby 只能读本地文件。这个项目做三件事：

1. **把网盘挂成目录** — 遍历网盘目录树，为每个视频生成 `.strm` 文件，内容是一个 HTTP 地址
2. **让 Emby 能播** — 内置反向代理，Emby 请求 `/d/xxx` 时由它去网盘取流并转发
3. **自动维护** — 定时同步新增、清理失效、刮削元数据、生成封面

全程一个容器，一个 Web 面板，数据落在本地 SQLite。

---

## 功能

**网盘接入**

- 115 网盘（账号密码 / Cookie / 开放平台）
- 阿里云盘（Token / 开放接口）
- 123 云盘
- AList（任意挂载源）

**媒体库**

- STRM 生成与增量同步
- Emby 反向代理（`/d/` `/s/` 路径直通，支持 Range 请求拖动进度条）
- TMDB 元数据刮削、剧集分季识别
- 封面生成（渐变 / 海报合成）
- 媒体目录监控与自动入库

**账号与权限**

- 多用户，JWT 认证
- 管理员 / 普通用户角色
- 面板登录、密码修改

**运维**

- 定时任务（同步、清理、签到、缓存刷新）
- 回收站清理
- 运行日志与任务日志
- 全量配置导入导出

---

## 架构

```
                    ┌──────────────────────────────────────┐
   浏览器  ────────► │  nginx  :9527                        │
                    │  ├─ /            静态面板 (Vue SPA)   │
                    │  └─ /api/ /d/ /s/  ──┐                │
                    └──────────────────────┼───────────────┘
                                           │
                    ┌──────────────────────▼───────────────┐
   Emby   ────────► │  nginx  :9096   （Emby 反代专用）     │
                    └──────────────────────┬───────────────┘
                                           │
                    ┌──────────────────────▼───────────────┐
                    │  cms-api  :9528  (仅容器内监听)       │
                    │  Python 3.12 · blacksheep · uvicorn   │
                    │  ├─ api/       HTTP 路由              │
                    │  ├─ core/      任务调度 / 授权 / 锁    │
                    │  ├─ modules/   网盘适配层              │
                    │  ├─ db/ dbv2/  SQLite 访问层           │
                    │  └─ services/  业务服务                │
                    └──────────────────────┬───────────────┘
                                           │
                    ┌──────────────────────▼───────────────┐
                    │  /config  (持久化)                    │
                    │  ├─ cms-online.db   SQLite 主库        │
                    │  ├─ 115-cookies.txt                   │
                    │  └─ backup/                           │
                    └──────────────────────────────────────┘
```

进程模型：`/entrypoint` 启动 nginx，然后 `exec python /cms/cms-api/app/main.py`。容器内 PID 1 是 Python 后端，nginx 作为子进程。

---

## 快速开始

### 1. 拿到镜像

从 [Releases](../../releases) 下载 `novamedia-v1.0.tar`，校验后导入：

```bash
sha256sum -c SHA256SUMS.txt
docker load -i novamedia-v1.0.tar
```

### 2. 起容器

```bash
git clone https://github.com/xhdyycx/media-cms.git
cd media-cms
cp .env.example .env        # 按需修改
docker compose up -d
```

### 3. 打开面板

```
http://<主机IP>:9527
```

默认账号 `admin` / `admin`，登录后**第一件事就是改密码**。

### 4. 接上 Emby

面板 → 设置 → Emby，填入 Emby 地址与 API Key。媒体库路径指向 STRM 输出目录。

---

## 端口

| 端口 | 用途 | 是否对外 |
|---|---|---|
| `9527` | Web 面板 + API 入口 | 是 |
| `9096` | Emby 反向代理（播放用） | 是 |
| `9528` | 后端服务 | **否**，仅容器内 |

播放地址形如 `http://<主机IP>:9096/d/<file_id>`，可直接填进 Emby 的媒体库路径。

---

## 目录结构

```
.
├── src/
│   ├── cms-api/          后端（Python）
│   │   ├── app/
│   │   │   ├── api/      HTTP 路由
│   │   │   ├── core/     调度、任务、授权、事件
│   │   │   ├── modules/  115 / 阿里 / 123 / AList / TMDB 适配
│   │   │   ├── db/       SQLite 访问层 v1
│   │   │   ├── dbv2/     SQLite 访问层 v2
│   │   │   ├── services/ 业务服务
│   │   │   └── utils/    工具函数
│   │   ├── sql/          初始化脚本
│   │   └── version.py
│   ├── web/              前端（Vue SPA，构建产物）
│   ├── embyExternalUrl/  Emby 外部链接工具（emby2Alist）
│   └── entrypoint        容器启动脚本
├── docs/                 文档
├── scripts/              安装与校验脚本
├── docker-compose.yml
└── .env.example
```

---

## 配置

所有配置通过环境变量传入，详见 [docs/configuration.md](docs/configuration.md)。

最常改的三个：

| 变量 | 说明 | 默认 |
|---|---|---|
| `TZ` | 时区 | `Asia/Shanghai` |
| `EMBY_HOST_PORT` | Emby 地址（容器视角） | `http://172.17.0.1:8096` |
| `EMBY_API_KEY` | Emby API Key | 空 |

`PUID` / `PGID` / `UMASK` 控制生成文件的属主，NAS 上通常需要设成你的用户 ID。

---

## 数据与备份

所有状态都在 `./config`：

| 文件 | 内容 |
|---|---|
| `cms-online.db` | 主库：账号、配置、媒体索引、任务记录 |
| `115-cookies.txt` | 115 登录态 |
| `backup/` | 自动备份 |

**迁移 = 拷走整个 `config` 目录**，换台机器起来即可。

`./logs` 是运行日志，可随时删。

---

## 开发

后端不依赖容器即可跑：

```bash
cd src/cms-api
pip install -r requirements.txt   # 若无，见 docs/deployment.md 手动装依赖
PYTHONPATH=. python app/main.py
```

前端是构建产物（`src/web/assets/`），改 UI 需要对应的 Vue 源码工程。

---

## 已知限制

- 镜像架构为 `linux/amd64`，ARM NAS 需自行构建
- 前端为打包产物，未附带 Vue 源工程
- 部分网盘接口依赖上游服务可用性

---

## 许可

MIT，见 [LICENSE](LICENSE)。随意使用、修改、分发，不提供任何担保。

---

## 相关

- [reversing-notes](https://github.com/xhdyycx/reversing-notes) — 这个项目在容器镜像、字节码还原、Windows 底层上踩过的坑

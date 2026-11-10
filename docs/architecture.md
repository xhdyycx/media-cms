# 架构

## 进程模型

容器启动后只有两个进程层级：

```
/entrypoint  (bash, PID 1 的父)
   ├── nginx -g "daemon off;"   → fork master + worker
   └── exec gosu cms:cms python /cms/cms-api/app/main.py   (PID 1)
```

`/entrypoint` 做四件事：

1. `groupmod` / `usermod` 把容器内 `cms` 用户的 UID/GID 改成 `PUID` / `PGID`
2. 准备 `/logs/nginx`，把 `$HOME`、`/config`、`/logs` 的属主交出去
3. 渲染 `constant.js`：把 `EMBY_HOST_PORT`、`EMBY_API_KEY`、`IMAGE_CACHE_POLICY`、`EMBY_LOCAL_FILE_PATH` 用 `sed` 写进 Emby 反代配置
4. 拉起 nginx，然后 `exec` 后端

`exec` 很关键 —— 后端直接接管 PID 1，SIGTERM 能正常传到 Python，`docker stop` 不会等 10 秒超时。

## 请求链路

### 面板

```
浏览器 :9527
   └─ nginx location /
        └─ root /cms/web  → index.html + assets/*
              └─ SPA 路由由前端接管
```

### API

```
浏览器 :9527/api/...
   └─ nginx location /api/
        └─ proxy_pass http://127.0.0.1:9528
             └─ blacksheep 路由 → api/ 下的 Controller
```

`9528` 只监听回环，宿主机扫不到，外部也连不上。想直接调试后端就把容器网络改成 host 模式。

### 播放

```
Emby :9096/d/<file_id>
   └─ nginx（独立的 server 块，带 Range / 分片支持）
        └─ proxy_pass http://127.0.0.1:9528
             └─ 后端向网盘取流，边下边转
```

`Range` 头必须透传，否则 Emby 拖动进度条会卡住或从头重下。

## 后端分层

| 目录 | 职责 |
|---|---|
| `app/api/` | HTTP 层。每个文件一个 Controller，`route()` 返回前缀，`@get` / `@post` 注册子路由 |
| `app/core/` | 调度与横切：`scheduler.py` 定时器、`task.py` 任务实现、`lock.py` 全局锁、`auth.py` 鉴权策略、`license.py` 授权状态、`event.py` 事件总线 |
| `app/modules/` | 网盘适配层。`ali/` 阿里、`alist/` AList、`hdhive/` 第三方接口、`media/` TMDB、`cover/` 封面合成 |
| `app/services/` | 业务服务，跨模块编排 |
| `app/db/` `app/dbv2/` | SQLite 访问层，两代并存 |
| `app/middleware/` | JWT 认证、请求日志 |
| `app/utils/` | 工具函数 |

## 数据流：从网盘到 Emby

```
  ① 遍历
  定时任务 → 网盘 API 列目录 → 写入媒体索引表

  ② 生成 STRM
  索引 → 每个视频生成 <name>.strm
        内容: http://<host>:9096/d/<file_id>

  ③ Emby 扫描
  Emby → 读 .strm → 请求 :9096/d/<file_id>

  ④ 取流
  nginx :9096 → 后端 :9528 → 网盘 API（带 Range）
             → 边收边转发给 Emby

  ⑤ 元数据
  定时任务 → TMDB 查询 → 写入剧集/电影信息 → 生成封面 nfo
```

## 存储

全部状态在 `/config`：

```
/config
├── cms-online.db          主库（SQLite）
├── cms-online.db.bak      自动备份
├── 115-cookies.txt        115 登录态
├── hdhive-openapi.json    第三方接口凭据
├── backup/                定时备份归档
└── constant.js            面板生成的 Emby 反代配置
```

数据库没有跨进程锁竞争 —— 只有后端一个进程写，`db/` 层自己维护连接池与事务边界。

## 前端

`src/web/` 是构建产物，不是源码：

```
web/
├── index.html          入口（<div id="app">）
└── assets/
    ├── index-*.js      主 bundle
    ├── index-*.css     样式
    └── *.js            按路由拆分的 chunk
```

修改 UI 需要对应的 Vue 工程重新构建，产物覆盖 `assets/` 即可，nginx 不需要改配置。

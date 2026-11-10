#!/usr/bin/env bash
# 安装后自检：镜像 / 容器 / 端口 / 接口 / 数据目录
set -uo pipefail

PASS=0; FAIL=0
ok()   { printf '  \033[32m✔\033[0m %s\n' "$*"; PASS=$((PASS+1)); }
bad()  { printf '  \033[31m✘\033[0m %s\n' "$*"; FAIL=$((FAIL+1)); }
head_(){ printf '\n\033[1m%s\033[0m\n' "$*"; }

head_ "1. 镜像"
if docker image inspect novamedia:v1.0 >/dev/null 2>&1; then
  SIZE=$(docker image inspect novamedia:v1.0 --format '{{.Size}}' | awk '{printf "%.2f GB", $1/1024/1024/1024}')
  ARCH=$(docker image inspect novamedia:v1.0 --format '{{.Architecture}}')
  ok "novamedia:v1.0 存在（$SIZE / $ARCH）"
else
  bad "镜像未导入"
fi

head_ "2. 容器"
if docker ps --format '{{.Names}}' | grep -qx media-cms; then
  STATUS=$(docker inspect media-cms --format '{{.State.Status}}')
  HEALTH=$(docker inspect media-cms --format '{{if .State.Health}}{{.State.Health.Status}}{{else}}n/a{{end}}')
  ok "media-cms 运行中（$STATUS / health=$HEALTH）"
  if docker logs media-cms 2>&1 | grep -q "Uvicorn running"; then
    ok "后端已监听"
  else
    bad "日志里没有 Uvicorn running"
  fi
else
  bad "容器 media-cms 未运行"
fi

head_ "3. 端口"
for p in 9527 9096; do
  if curl -fsS -o /dev/null --max-time 5 "http://127.0.0.1:$p/" 2>/dev/null; then
    ok "$p 有响应"
  else
    bad "$p 无响应"
  fi
done
if curl -fsS -o /dev/null --max-time 3 "http://127.0.0.1:9528/" 2>/dev/null; then
  bad "9528 从宿主机可达（应只在容器内）"
else
  ok "9528 未对外暴露"
fi

head_ "4. 接口"
LOGIN=$(curl -fsS --max-time 10 -X POST "http://127.0.0.1:9527/api/auth/login" \
  -H 'Content-Type: application/json' \
  -d '{"username":"admin","password":"admin"}' 2>/dev/null || true)
if echo "$LOGIN" | grep -q '"token"'; then
  ok "登录接口正常"
  VER=$(echo "$LOGIN" | sed -n 's/.*"version":"\([^"]*\)".*/\1/p')
  [ -n "$VER" ] && ok "后端版本: $VER"
else
  bad "登录失败，响应: ${LOGIN:0:120}"
fi

head_ "5. 数据目录"
[ -d config ] && ok "config/ 存在" || bad "config/ 不存在"
[ -f config/cms-online.db ] && ok "数据库已初始化（$(du -h config/cms-online.db | cut -f1)）" || bad "数据库未初始化"
[ -d logs ] && ok "logs/ 存在" || bad "logs/ 不存在"

head_ "结果"
printf '  通过 %d 项，失败 %d 项\n\n' "$PASS" "$FAIL"
[ "$FAIL" -eq 0 ] && exit 0 || exit 1

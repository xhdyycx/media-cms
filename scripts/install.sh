#!/usr/bin/env bash
# Media CMS 一键安装
#   用法: ./scripts/install.sh [镜像路径]
set -euo pipefail

IMAGE_TAR="${1:-novamedia-v1.0.tar}"
IMAGE_TAG="novamedia:v1.0"

say() { printf '\033[1;36m[install]\033[0m %s\n' "$*"; }
die() { printf '\033[1;31m[error]\033[0m %s\n' "$*" >&2; exit 1; }

# ── 1. 环境检查 ─────────────────────────────────────────
command -v docker >/dev/null 2>&1 || die "没找到 docker，先装 Docker"
docker info >/dev/null 2>&1 || die "docker 守护进程没起来（权限或未启动）"

if docker compose version >/dev/null 2>&1; then
  COMPOSE="docker compose"
elif command -v docker-compose >/dev/null 2>&1; then
  COMPOSE="docker-compose"
else
  die "没找到 docker compose"
fi

# ── 2. 镜像校验 ─────────────────────────────────────────
[ -f "$IMAGE_TAR" ] || die "找不到镜像文件: $IMAGE_TAR"

if [ -f SHA256SUMS.txt ]; then
  say "校验镜像完整性…"
  EXPECT=$(grep -F "$(basename "$IMAGE_TAR")" SHA256SUMS.txt | awk '{print $1}' || true)
  if [ -n "$EXPECT" ]; then
    ACTUAL=$(sha256sum "$IMAGE_TAR" | awk '{print $1}')
    if [ "$EXPECT" != "$ACTUAL" ]; then
      die "SHA256 不匹配
     期望: $EXPECT
     实际: $ACTUAL
     文件可能下载不完整，请重新下载"
    fi
    say "校验通过"
  fi
fi

# ── 3. 导入镜像 ─────────────────────────────────────────
if docker image inspect "$IMAGE_TAG" >/dev/null 2>&1; then
  say "镜像 $IMAGE_TAG 已存在，跳过导入"
else
  say "导入镜像（约 1.1 GB，需要一会儿）…"
  docker load -i "$IMAGE_TAR"
fi

# ── 4. 准备配置 ─────────────────────────────────────────
[ -f .env ] || { cp .env.example .env; say "已生成 .env，按需修改后启动"; }
mkdir -p config logs

# ── 5. 启动 ─────────────────────────────────────────────
say "启动容器…"
$COMPOSE up -d

# ── 6. 等就绪 ───────────────────────────────────────────
say "等待服务就绪…"
for i in $(seq 1 30); do
  if curl -fsS -o /dev/null "http://127.0.0.1:9527/" 2>/dev/null; then
    break
  fi
  sleep 2
  [ "$i" -eq 30 ] && { say "超时，看日志: $COMPOSE logs --tail 50"; exit 1; }
done

IP=$(hostname -I 2>/dev/null | awk '{print $1}')
[ -z "$IP" ] && IP="<本机IP>"

cat <<EOF

  ────────────────────────────────────────────
   安装完成

   面板    http://$IP:9527
   账号    admin / admin     ← 登录后立刻改密码
   播放    http://$IP:9096/d/<file_id>
   数据    ./config
  ────────────────────────────────────────────

EOF

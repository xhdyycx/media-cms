import importlib
from pathlib import Path

from alembic.config import Config as AlembicConfig
from alembic.command import revision as alembic_revision

from app.core.env import cmsEnv

# 导入模块，避免建表缺失
models_path = Path(__file__).parent.parent / "app" / "db" / "models"
# print(models_path)
for module in models_path.glob("*.py"):
    if module.stem != "__init__":  # 排除 __init__.py
        importlib.import_module(f"app.db.models.{module.stem}")

db_version = input("请输入版本号：")
script_location = cmsEnv.ROOT_PATH / 'sql'
alembic_cfg = AlembicConfig()
alembic_cfg.set_main_option('script_location', str(script_location))
alembic_cfg.set_main_option('sqlalchemy.url', cmsEnv.DATABASE_SQL)

# 生成增量迁移
alembic_revision(alembic_cfg, db_version, autogenerate=True)

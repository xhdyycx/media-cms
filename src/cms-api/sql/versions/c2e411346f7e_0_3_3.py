"""7

Revision ID: c2e411346f7e
Revises:
Create Date: 2025-01-15 20:36:49.881301

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.exc import SQLAlchemyError
from app.log import logger

# revision identifiers, used by Alembic.
revision = 'c2e411346f7e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # 清理重复数据
    op.execute(
        "DELETE FROM cloud_data WHERE id NOT IN (SELECT MIN(id) FROM cloud_data GROUP BY fid) AND fid IN (SELECT fid FROM cloud_data GROUP BY fid HAVING COUNT(*) > 1);")

    # 删除临时表和索引
    op.execute("DROP TABLE IF EXISTS _alembic_tmp_cloud_data;")
    op.execute("DROP INDEX IF EXISTS ix_cloud_data_pid;")
    op.execute("DROP INDEX IF EXISTS ix_cloud_data_sha1;")

    try:
        with op.batch_alter_table('cloud_data', schema=None) as batch_op:
            batch_op.drop_constraint('uix_cloud_data_fid', type_='unique')
    except Exception as e:
        pass

    try:
        with op.batch_alter_table('cloud_data', schema=None) as batch_op:
            batch_op.drop_constraint('uix_cloud_data_pick_code', type_='unique')
    except Exception as e:
        pass

    with op.batch_alter_table('cloud_data', schema=None) as batch_op:
        # 创建新的索引和约束
        batch_op.create_index('ix_cloud_data_pid', ['pid'], unique=False)
        batch_op.create_index('ix_cloud_data_sha1', ['sha1'], unique=False)
        batch_op.create_unique_constraint('uix_cloud_data_fid', ['fid'])

    # 更新状态
    op.execute("UPDATE cloud_data SET status = 1")


def downgrade() -> None:
    pass

"""empty message

Revision ID: b229ec19dec9
Revises: edc3ea775e68
Create Date: 2022-09-05 12:23:12.476017

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'b229ec19dec9'
down_revision = 'edc3ea775e68'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('cluster_logs', 'cluster_id',
               existing_type=postgresql.UUID(),
               nullable=True)
    op.drop_constraint('cluster_logs_cluster_id_fkey', 'cluster_logs', type_='foreignkey')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key('cluster_logs_cluster_id_fkey', 'cluster_logs', 'clusters', ['cluster_id'], ['id'])
    op.alter_column('cluster_logs', 'cluster_id',
               existing_type=postgresql.UUID(),
               nullable=False)
    # ### end Alembic commands ###

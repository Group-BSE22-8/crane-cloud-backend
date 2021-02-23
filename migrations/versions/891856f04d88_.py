"""empty message

Revision ID: 891856f04d88
Revises: b85cd508eff7
Create Date: 2021-02-23 12:04:27.017337

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '891856f04d88'
down_revision = 'b85cd508eff7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('project_database', sa.Column('host', sa.String(length=256), nullable=True))
    op.add_column('project_database', sa.Column('name', sa.String(length=256), nullable=False))
    op.add_column('project_database', sa.Column('password', sa.String(length=256), nullable=False))
    op.add_column('project_database', sa.Column('user', sa.String(length=256), nullable=False))
    op.drop_column('project_database', 'database_host')
    op.drop_column('project_database', 'database_password')
    op.drop_column('project_database', 'database_user')
    op.drop_column('project_database', 'database_name')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('project_database', sa.Column('database_name', sa.VARCHAR(length=256), autoincrement=False, nullable=False))
    op.add_column('project_database', sa.Column('database_user', sa.VARCHAR(length=256), autoincrement=False, nullable=False))
    op.add_column('project_database', sa.Column('database_password', sa.VARCHAR(length=256), autoincrement=False, nullable=False))
    op.add_column('project_database', sa.Column('database_host', sa.VARCHAR(length=256), autoincrement=False, nullable=True))
    op.drop_column('project_database', 'user')
    op.drop_column('project_database', 'password')
    op.drop_column('project_database', 'name')
    op.drop_column('project_database', 'host')
    # ### end Alembic commands ###

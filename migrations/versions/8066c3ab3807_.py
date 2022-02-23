"""empty message

Revision ID: 8066c3ab3807
Revises: 371b602785d5
Create Date: 2022-02-23 13:24:30.781081

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '8066c3ab3807'
down_revision = '371b602785d5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('project_cluster',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('cluster_id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('project_id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.ForeignKeyConstraint(['cluster_id'], ['clusters.id'], ),
    sa.ForeignKeyConstraint(['project_id'], ['project.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('project_cluster')
    # ### end Alembic commands ###

"""empty message

Revision ID: 7844dd65a476
Revises: 
Create Date: 2022-02-24 17:19:43.712869

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7844dd65a476'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('states',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('acronym', sa.String(length=2), nullable=False),
    sa.Column('population', sa.Integer(), nullable=True),
    sa.Column('area', sa.DECIMAL(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('acronym'),
    sa.UniqueConstraint('name')
    )
    op.create_table('capitals',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=80), nullable=False),
    sa.Column('neighborhoods', sa.String(length=255), nullable=True),
    sa.Column('population', sa.Integer(), nullable=True),
    sa.Column('state_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['state_id'], ['states.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name'),
    sa.UniqueConstraint('state_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('capitals')
    op.drop_table('states')
    # ### end Alembic commands ###
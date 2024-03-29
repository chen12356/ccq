"""empty message

Revision ID: 749692e2daec
Revises: 
Create Date: 2019-09-22 21:46:19.324181

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '749692e2daec'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('emp_info',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('username', sa.String(length=32), nullable=True),
    sa.Column('name', sa.String(length=32), nullable=True),
    sa.Column('password', sa.String(length=32), nullable=True),
    sa.Column('sex', sa.String(length=8), nullable=True),
    sa.Column('age', sa.Integer(), nullable=True),
    sa.Column('phone', sa.Integer(), nullable=True),
    sa.Column('ask', sa.String(length=256), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('phone')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('emp_info')
    # ### end Alembic commands ###

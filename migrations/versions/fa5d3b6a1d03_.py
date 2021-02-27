"""empty message

Revision ID: fa5d3b6a1d03
Revises: 17c4c20827d6
Create Date: 2021-02-27 17:19:52.163534

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'fa5d3b6a1d03'
down_revision = '17c4c20827d6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('planets',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('diameter', sa.Integer(), nullable=False),
    sa.Column('population', sa.String(length=80), nullable=False),
    sa.Column('surface_water', sa.Integer(), nullable=False),
    sa.Column('gravity', sa.String(length=80), nullable=False),
    sa.Column('climate', sa.String(length=50), nullable=False),
    sa.Column('terrain', sa.String(length=50), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('url', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('planetas')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('planetas',
    sa.Column('id', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('diameter', mysql.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('population', mysql.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('surface_water', mysql.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('gravity', mysql.VARCHAR(length=80), nullable=False),
    sa.Column('climate', mysql.VARCHAR(length=50), nullable=False),
    sa.Column('terrain', mysql.VARCHAR(length=50), nullable=False),
    sa.Column('name', mysql.VARCHAR(length=50), nullable=False),
    sa.Column('url', mysql.VARCHAR(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.drop_table('planets')
    # ### end Alembic commands ###

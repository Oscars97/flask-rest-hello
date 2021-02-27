"""empty message

Revision ID: aa970dc1a712
Revises: fa5d3b6a1d03
Create Date: 2021-02-27 17:35:35.912186

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'aa970dc1a712'
down_revision = 'fa5d3b6a1d03'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('personajes', sa.Column('tipo', sa.String(length=50), nullable=False))
    op.add_column('planets', sa.Column('tipo', sa.String(length=50), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('planets', 'tipo')
    op.drop_column('personajes', 'tipo')
    # ### end Alembic commands ###

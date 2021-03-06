"""empty message

Revision ID: d2ba5ef6d26d
Revises: 
Create Date: 2020-08-18 17:47:56.563418

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd2ba5ef6d26d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('pessoa',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('cpf', sa.String(length=14), nullable=False),
    sa.Column('nome', sa.String(length=40), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('cpf'),
    sa.UniqueConstraint('nome')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('pessoa')
    # ### end Alembic commands ###

"""1m

Revision ID: 0a4357bc422e
Revises: 
Create Date: 2023-04-22 14:21:48.259846

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0a4357bc422e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('alphabank',
    sa.Column('bank_sell', sa.Float(), nullable=False),
    sa.Column('bank_buy', sa.Float(), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('sell_currency', sa.String(length=50), nullable=False),
    sa.Column('buy_currency', sa.String(length=50), nullable=False),
    sa.Column('time_get_data', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('balapb',
    sa.Column('convert', sa.Float(), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('sell_currency', sa.String(length=50), nullable=False),
    sa.Column('buy_currency', sa.String(length=50), nullable=False),
    sa.Column('time_get_data', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('belarusbank',
    sa.Column('bank_sell', sa.Float(), nullable=False),
    sa.Column('bank_buy', sa.Float(), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('sell_currency', sa.String(length=50), nullable=False),
    sa.Column('buy_currency', sa.String(length=50), nullable=False),
    sa.Column('time_get_data', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('nbrb',
    sa.Column('convert', sa.Float(), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('sell_currency', sa.String(length=50), nullable=False),
    sa.Column('buy_currency', sa.String(length=50), nullable=False),
    sa.Column('time_get_data', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_name', sa.String(length=30), nullable=False),
    sa.Column('email', sa.String(length=320), nullable=False),
    sa.Column('hashed_password', sa.String(length=1024), nullable=False),
    sa.Column('is_active', sa.Boolean(), nullable=False),
    sa.Column('is_superuser', sa.Boolean(), nullable=False),
    sa.Column('is_verified', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_email'), 'user', ['email'], unique=True)
    op.create_index(op.f('ix_user_id'), 'user', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_user_id'), table_name='user')
    op.drop_index(op.f('ix_user_email'), table_name='user')
    op.drop_table('user')
    op.drop_table('nbrb')
    op.drop_table('belarusbank')
    op.drop_table('balapb')
    op.drop_table('alphabank')
    # ### end Alembic commands ###
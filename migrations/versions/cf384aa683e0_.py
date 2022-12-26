"""empty message

Revision ID: cf384aa683e0
Revises: 
Create Date: 2022-06-20 11:55:17.763832

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cf384aa683e0'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('card_request',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('card', sa.String(length=30), nullable=False),
    sa.Column('first_name', sa.String(length=30), nullable=False),
    sa.Column('last_name', sa.String(length=30), nullable=False),
    sa.Column('code', sa.Integer(), nullable=False),
    sa.Column('prefix', sa.String(length=30), nullable=False),
    sa.Column('p_number', sa.String(length=30), nullable=False),
    sa.Column('branch', sa.String(length=30), nullable=False),
    sa.Column('file1', sa.String(length=255), nullable=False),
    sa.Column('file2', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('cards',
    sa.Column('card_id', sa.Integer(), nullable=False),
    sa.Column('card_header', sa.String(length=30), nullable=False),
    sa.Column('card_info', sa.Text(), nullable=False),
    sa.Column('term', sa.String(length=30), nullable=False),
    sa.Column('currency', sa.String(length=30), nullable=False),
    sa.Column('cashback', sa.String(length=30), nullable=False),
    sa.PrimaryKeyConstraint('card_id')
    )
    op.create_table('loan_request',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(length=30), nullable=False),
    sa.Column('last_name', sa.String(length=30), nullable=False),
    sa.Column('job', sa.String(length=30), nullable=False),
    sa.Column('prefix', sa.String(length=30), nullable=False),
    sa.Column('p_number', sa.String(length=30), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('loans',
    sa.Column('loan_id', sa.Integer(), nullable=False),
    sa.Column('loan_header', sa.String(length=30), nullable=False),
    sa.Column('loan_info', sa.Text(), nullable=False),
    sa.Column('amount', sa.String(length=30), nullable=False),
    sa.Column('term', sa.String(length=30), nullable=False),
    sa.Column('int_payment', sa.String(length=30), nullable=False),
    sa.PrimaryKeyConstraint('loan_id')
    )
    op.create_table('news',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=255), nullable=False),
    sa.Column('created_at', sa.Date(), nullable=True),
    sa.Column('news_content', sa.Text(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('role',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=100), nullable=True),
    sa.Column('password', sa.String(length=255), nullable=True),
    sa.Column('active', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('roles_users',
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('role_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['role_id'], ['role.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('roles_users')
    op.drop_table('user')
    op.drop_table('role')
    op.drop_table('news')
    op.drop_table('loans')
    op.drop_table('loan_request')
    op.drop_table('cards')
    op.drop_table('card_request')
    # ### end Alembic commands ###
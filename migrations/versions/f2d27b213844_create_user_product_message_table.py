"""Create User,Product,Message table

Revision ID: f2d27b213844
Revises: 
Create Date: 2023-07-06 11:11:15.289423

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f2d27b213844'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'users',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(length=50), nullable=True),
        sa.Column('email', sa.String(length=100), nullable=False),
        sa.Column('password', sa.String(length=100), nullable=False),
        sa.Column('confirm_password', sa.String(length=100), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('email')
    )
    op.create_table(
        'products',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('title', sa.String(length=20), nullable=True),
        sa.Column('productDescription', sa.String(length=100), nullable=True),
        sa.Column('productBrand', sa.String(length=20), nullable=True),
        sa.Column('price', sa.Integer(), nullable=True),
        sa.Column('user_id', sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(['user_id'], ['users.id']),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_table(
        'messages',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('message', sa.String(length=100), nullable=True),
        sa.Column('sender_id', sa.Integer(), nullable=True),
        sa.Column('receiver_id', sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(['sender_id'], ['users.id']),
        sa.ForeignKeyConstraint(['receiver_id'], ['users.id']),
        sa.PrimaryKeyConstraint('id')
    )

def downgrade():
    op.drop_table('messages')
    op.drop_table('products')
    op.drop_table('users')

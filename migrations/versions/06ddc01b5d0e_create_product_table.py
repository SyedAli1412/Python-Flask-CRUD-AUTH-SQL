"""create Product table

Revision ID: 06ddc01b5d0e
Revises: 8d4eee8582df
Create Date: 2023-07-04 16:22:37.679961

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '06ddc01b5d0e'
down_revision = '8d4eee8582df'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'products',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('title', sa.String(length=20), nullable=True),
        sa.Column('productDescription', sa.String(length=100), nullable=True),
        sa.Column('productBrand', sa.String(length=20), nullable=True),
        sa.Column('price', sa.Integer(), nullable=True),
        sa.Column('user_id', sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
        sa.PrimaryKeyConstraint('id')
    )


def downgrade():
    op.drop_table('products')

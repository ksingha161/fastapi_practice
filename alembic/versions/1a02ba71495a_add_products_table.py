"""add products table

Revision ID: 1a02ba71495a
Revises: 
Create Date: 2021-12-24 14:09:39.027541

"""
from datetime import time
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1a02ba71495a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('products', sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
                    sa.Column('product_type', sa.String(), nullable=False),
                    sa.Column('price', sa.Numeric(), nullable=False),
                    sa.Column('is_purchased', sa.Boolean(), nullable=False, server_default='TRUE'),
                    sa.Column('created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('NOW()')))
    pass

def downgrade():
    op.drop_table('products')
    pass

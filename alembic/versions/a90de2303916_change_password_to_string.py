"""change password to string

Revision ID: a90de2303916
Revises: a10c12f51469
Create Date: 2021-12-24 14:32:57.905487

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a90de2303916'
down_revision = 'a10c12f51469'
branch_labels = None
depends_on = None


def upgrade():
    op.alter_column('users', 'password', type_=sa.String())
    pass


def downgrade():
    op.drop_column('users', 'password')
    pass

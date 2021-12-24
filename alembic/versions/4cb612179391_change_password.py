"""change password

Revision ID: 4cb612179391
Revises: a90de2303916
Create Date: 2021-12-24 14:43:39.153601

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4cb612179391'
down_revision = 'a90de2303916'
branch_labels = None
depends_on = None


def upgrade():
    op.alter_column('users', 'password', type_=sa.String(), existing_type=sa.Numeric(), nullable=False, existing_nullable=True)
    pass


def downgrade():
    op.drop_column('users', 'password')
    pass

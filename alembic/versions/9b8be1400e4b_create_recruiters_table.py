"""create recruiters table

Revision ID: 9b8be1400e4b
Revises: 7d08c90c8f82
Create Date: 2022-11-03 15:14:53.146810

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9b8be1400e4b'
down_revision = '7d08c90c8f82'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('recruiters',
    sa.Column('id', sa.Integer, primary_key=True, nullable=False),
    sa.Column('created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('now()')),
    sa.Column('status', sa.String, nullable=False, server_default='active'),
    sa.Column('company_name', sa.String),
    sa.Column('email', sa.String, nullable=False, unique=True),
    sa.Column('password', sa.String, nullable=False)                
    )


def downgrade() -> None:
    op.drop_table('recruiters')

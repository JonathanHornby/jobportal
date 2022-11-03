"""create users table

Revision ID: 7d08c90c8f82
Revises: 
Create Date: 2022-11-03 14:59:55.537307

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7d08c90c8f82'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('users',
    sa.Column('id', sa.Integer, primary_key=True, nullable=False),
    sa.Column('created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('now()')),
    sa.Column('status', sa.String, nullable=False, server_default='active'),
    sa.Column('name', sa.String),
    sa.Column('email', sa.String, nullable=False, unique=True),
    sa.Column('password', sa.String, nullable=False)
    )


def downgrade() -> None:
    op.drop_table('users')
    pass

"""create jobs table

Revision ID: bd4eb7315b4b
Revises: 9b8be1400e4b
Create Date: 2022-11-03 15:17:51.359745

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bd4eb7315b4b'
down_revision = '9b8be1400e4b'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('jobs',
    sa.Column('id', sa.Integer, primary_key=True, nullable=False),
    sa.Column('poster_id', sa.Integer, nullable=False),
    sa.ForeignKeyConstraint(('poster_id',), ['recruiters.id'],),
    sa.Column('created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('now()')),
    sa.Column('status', sa.String, nullable=False, server_default='active'),
    sa.Column('published', sa.Boolean, server_default='FALSE', nullable=False),
    sa.Column('product_type', sa.Integer, nullable=False, server_default=sa.text('1')),
    sa.Column('valid_duration', sa.Integer, nullable=False, server_default=sa.text('30')),
    sa.Column('title', sa.String),
    sa.Column('company', sa.String),
    sa.Column('country', sa.String),
    sa.Column('state', sa.String),
    sa.Column('city', sa.String),
    sa.Column('industry', sa.String),
    sa.Column('category', sa.String),
    sa.Column('employment_type', sa.String),
    sa.Column('remote_status', sa.String),
    sa.Column('salary_min', sa.Integer),
    sa.Column('salary_max', sa.Integer),
    sa.Column('salary_currency', sa.String),
    sa.Column('summary', sa.Text),
    sa.Column('content', sa.Text),
    sa.Column('contact_name', sa.String),
    sa.Column('contact_number', sa.String),
    sa.Column('perk_car', sa.Boolean, nullable=False, server_default=sa.text('False')),
    sa.Column('perk_visa', sa.Boolean, nullable=False, server_default=sa.text('False')),
    sa.Column('perk_relocation', sa.Boolean, nullable=False, server_default=sa.text('False')),
    sa.Column('perk_days_week', sa.Integer, nullable=False, server_default=sa.text('5')),
    sa.Column('perk_phone', sa.Boolean, nullable=False, server_default=sa.text('False')),
    sa.Column('perk_laptop', sa.Boolean, nullable=False, server_default=sa.text('False')),
    sa.Column('perk_bonus', sa.Boolean, nullable=False, server_default=sa.text('False'))    
    )


def downgrade() -> None:
    pass

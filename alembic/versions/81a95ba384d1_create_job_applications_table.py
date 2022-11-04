"""Create job applications table

Revision ID: 81a95ba384d1
Revises: bd4eb7315b4b
Create Date: 2022-11-04 10:32:50.772717

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '81a95ba384d1'
down_revision = 'bd4eb7315b4b'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('job_applications',
    sa.Column('created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('now()')),
    sa.Column('recruiter_status', sa.String, nullable=False, server_default='new'),
    sa.Column('user_id', sa.Integer, primary_key=True, nullable=False),
    sa.ForeignKeyConstraint(('user_id',), ['users.id'],),
    sa.Column('job_id', sa.Integer, primary_key=True, nullable=False),
    sa.ForeignKeyConstraint(('job_id',), ['jobs.id'],),
    sa.Column('cv_path', sa.String),
    sa.Column('cover_letter_path', sa.String)
    )


def downgrade() -> None:
    op.drop_table('job_applications')


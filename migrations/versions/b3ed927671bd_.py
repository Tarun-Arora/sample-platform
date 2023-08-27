"""Add last_passed_on and description fields in regression_test

Revision ID: b3ed927671bd
Revises: a5183973c3e9
Create Date: 2023-08-17 00:41:01.237549

"""
import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'b3ed927671bd'
down_revision = 'a5183973c3e9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('regression_test', schema=None) as batch_op:
        batch_op.add_column(sa.Column('last_passed_on', sa.Integer(), nullable=True))
        batch_op.create_foreign_key('regression_test_ibfk_2', 'test', ['last_passed_on'], ['id'], onupdate='CASCADE', ondelete='SET NULL')
        batch_op.add_column(sa.Column('description', sa.String(length=1024), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('regression_test', schema=None) as batch_op:
        batch_op.drop_constraint('regression_test_ibfk_2', type_='foreignkey')
        batch_op.drop_column('last_passed_on')
        batch_op.drop_column('description')
    # ### end Alembic commands ###

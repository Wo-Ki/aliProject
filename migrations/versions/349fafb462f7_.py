"""empty message

Revision ID: 349fafb462f7
Revises: 0f2091bea637
Create Date: 2018-04-06 09:16:01.103792

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '349fafb462f7'
down_revision = '0f2091bea637'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('production', 'image1',
               existing_type=sa.BLOB(),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('production', 'image1',
               existing_type=sa.BLOB(),
               nullable=False)
    # ### end Alembic commands ###

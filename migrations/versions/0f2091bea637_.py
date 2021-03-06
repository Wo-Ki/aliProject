"""empty message

Revision ID: 0f2091bea637
Revises: 8f2c7156b445
Create Date: 2018-04-05 19:05:54.024703

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '0f2091bea637'
down_revision = '8f2c7156b445'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('comment', sa.Column('production_id', sa.Integer(), nullable=True))
    op.drop_constraint(u'comment_ibfk_1', 'comment', type_='foreignkey')
    op.create_foreign_key(None, 'comment', 'production', ['production_id'], ['id'])
    op.drop_column('comment', 'comment_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('comment', sa.Column('comment_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'comment', type_='foreignkey')
    op.create_foreign_key(u'comment_ibfk_1', 'comment', 'production', ['comment_id'], ['id'])
    op.drop_column('comment', 'production_id')
    # ### end Alembic commands ###

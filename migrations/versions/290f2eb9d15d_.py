"""empty message

Revision ID: 290f2eb9d15d
Revises: 
Create Date: 2018-04-01 08:54:18.629231

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '290f2eb9d15d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=50), nullable=False),
    sa.Column('password', sa.String(length=100), nullable=False),
    sa.Column('email', sa.String(length=50), nullable=False),
    sa.Column('telephone', sa.String(length=20), nullable=True),
    sa.Column('qqNum', sa.String(length=50), nullable=True),
    sa.Column('headPic', sa.BLOB(), nullable=True),
    sa.Column('sex', sa.Integer(), nullable=True),
    sa.Column('birthday', sa.DateTime(), nullable=True),
    sa.Column('signature', sa.Text(), nullable=True),
    sa.Column('isComment', sa.Boolean(), nullable=True),
    sa.Column('create_time', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('production',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=50), nullable=False),
    sa.Column('content', sa.Text(), nullable=True),
    sa.Column('insertPic_0', sa.BLOB(), nullable=False),
    sa.Column('insertPic_1', sa.BLOB(), nullable=True),
    sa.Column('insertPic_2', sa.BLOB(), nullable=True),
    sa.Column('insertPic_3', sa.BLOB(), nullable=True),
    sa.Column('insertPic_4', sa.BLOB(), nullable=True),
    sa.Column('price', sa.Integer(), nullable=False),
    sa.Column('province', sa.String(length=50), nullable=True),
    sa.Column('city', sa.String(length=50), nullable=True),
    sa.Column('viewNum', sa.Integer(), nullable=False),
    sa.Column('commitNum', sa.Integer(), nullable=False),
    sa.Column('create_time', sa.DateTime(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('comment',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('isRead', sa.Boolean(), nullable=True),
    sa.Column('create_time', sa.DateTime(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('comment_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['comment_id'], ['production.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('comment')
    op.drop_table('production')
    op.drop_table('user')
    # ### end Alembic commands ###

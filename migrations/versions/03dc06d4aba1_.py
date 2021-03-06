"""empty message

Revision ID: 03dc06d4aba1
Revises: 3cd2428090dd
Create Date: 2022-04-11 15:29:47.882005

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '03dc06d4aba1'
down_revision = '3cd2428090dd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('success_stories',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=100), nullable=False),
    sa.Column('story', sa.String(length=500), nullable=False),
    sa.Column('date', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('success_stories')
    # ### end Alembic commands ###

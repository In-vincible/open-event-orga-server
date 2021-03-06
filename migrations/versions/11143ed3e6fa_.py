"""empty message

Revision ID: 11143ed3e6fa
Revises: 94e639e6575c
Create Date: 2016-12-31 17:35:45.270991

"""

# revision identifiers, used by Alembic.
revision = '11143ed3e6fa'
down_revision = '94e639e6575c'

from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('speaker', sa.Column('speaking_experience', sa.Text(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('speaker', 'speaking_experience')
    ### end Alembic commands ###

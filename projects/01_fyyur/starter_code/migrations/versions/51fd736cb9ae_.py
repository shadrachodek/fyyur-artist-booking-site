"""empty message

Revision ID: 51fd736cb9ae
Revises: d4e37e024a71
Create Date: 2022-06-03 15:39:15.226509

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '51fd736cb9ae'
down_revision = 'd4e37e024a71'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('artists', sa.Column('created_at', sa.DateTime(), nullable=False))
    op.add_column('venues', sa.Column('created_at', sa.DateTime(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('venues', 'created_at')
    op.drop_column('artists', 'created_at')
    # ### end Alembic commands ###

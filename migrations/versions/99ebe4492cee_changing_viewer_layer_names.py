"""changing viewer layer names

Revision ID: 99ebe4492cee
Revises: b0b51fd07bfa
Create Date: 2023-06-12 15:34:29.609937

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '99ebe4492cee'
down_revision = 'b0b51fd07bfa'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('datastack', sa.Column('viewer_layer_name', sa.String(length=100), nullable=True))
    op.add_column('image_source', sa.Column('viewer_layer_name', sa.String(length=100), nullable=True))
    op.drop_column('image_source', 'ngl_layer_name')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('image_source', sa.Column('ngl_layer_name', sa.VARCHAR(length=100), autoincrement=False, nullable=True))
    op.drop_column('image_source', 'viewer_layer_name')
    op.drop_column('datastack', 'viewer_layer_name')
    # ### end Alembic commands ###

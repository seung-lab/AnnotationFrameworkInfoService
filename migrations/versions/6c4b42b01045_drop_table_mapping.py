"""drop table mapping

Revision ID: 6c4b42b01045
Revises: 9e8b9d192ad8
Create Date: 2022-04-12 09:13:37.540255

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6c4b42b01045'
down_revision = '9e8b9d192ad8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('tablemapping')
    op.drop_table('permissiongroup')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('permissiongroup',
    sa.Column('id', sa.INTEGER(), server_default=sa.text("nextval('permissiongroup_id_seq'::regclass)"), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(length=100), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='permissiongroup_pkey'),
    sa.UniqueConstraint('name', name='permissiongroup_uniq'),
    postgresql_ignore_search_path=False
    )
    op.create_table('tablemapping',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('table_name', sa.VARCHAR(length=100), autoincrement=False, nullable=False),
    sa.Column('service_name', sa.VARCHAR(length=100), autoincrement=False, nullable=False),
    sa.Column('permissiongroup_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['permissiongroup_id'], ['permissiongroup.id'], name='tablemapping_permissiongroup_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='tablemapping_pkey')
    )
    # ### end Alembic commands ###

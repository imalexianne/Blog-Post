"""Delete Column

Revision ID: 13f644585c18
Revises: f098deca83e3
Create Date: 2019-03-04 17:50:20.814015

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '13f644585c18'
down_revision = 'f098deca83e3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('comments', 'author')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('comments', sa.Column('author', sa.VARCHAR(length=255), autoincrement=False, nullable=True))
    # ### end Alembic commands ###

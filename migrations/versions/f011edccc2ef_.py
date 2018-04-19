"""empty message

Revision ID: f011edccc2ef
Revises: 05f123d35ee9
Create Date: 2018-02-16 15:52:59.306912

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f011edccc2ef'
down_revision = '05f123d35ee9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('variants', sa.Column('variant_id', sa.String(length=50000), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('variants', 'variant_id')
    # ### end Alembic commands ###
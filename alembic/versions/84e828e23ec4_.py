"""???

Revision ID: 84e828e23ec4
Revises: 03e7726dd38a
Create Date: 2023-10-09 17:23:53.879426

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '84e828e23ec4'
down_revision = '03e7726dd38a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('donation',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('full_amount', sa.Integer(), nullable=False),
    sa.Column('invested_amount', sa.Integer(), nullable=True),
    sa.Column('fully_invested', sa.Boolean(), nullable=True),
    sa.Column('create_date', sa.DateTime(), nullable=True),
    sa.Column('close_date', sa.DateTime(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('comment', sa.Text(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('donation')
    # ### end Alembic commands ###

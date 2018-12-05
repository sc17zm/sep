"""empty message

Revision ID: 8f42528f623b
Revises: cb988e5a6000
Create Date: 2018-12-04 13:49:37.633602

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8f42528f623b'
down_revision = 'cb988e5a6000'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('expert',
    sa.Column('expertid', sa.String(length=6), nullable=False),
    sa.Column('expertpassword', sa.String(length=8), nullable=True),
    sa.PrimaryKeyConstraint('expertid')
    )
    op.create_table('student',
    sa.Column('studentid', sa.String(length=6), nullable=False),
    sa.Column('studentpassword', sa.String(length=8), nullable=True),
    sa.PrimaryKeyConstraint('studentid')
    )
    op.drop_table('student_login')
    op.drop_table('expert_login')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('expert_login',
    sa.Column('expertid', sa.VARCHAR(length=6), nullable=False),
    sa.Column('expertpassword', sa.VARCHAR(length=8), nullable=True),
    sa.PrimaryKeyConstraint('expertid')
    )
    op.create_table('student_login',
    sa.Column('studentid', sa.VARCHAR(length=6), nullable=False),
    sa.Column('studentpassword', sa.VARCHAR(length=8), nullable=True),
    sa.PrimaryKeyConstraint('studentid')
    )
    op.drop_table('student')
    op.drop_table('expert')
    # ### end Alembic commands ###
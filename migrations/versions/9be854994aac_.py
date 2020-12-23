"""empty message

Revision ID: 9be854994aac
Revises: 
Create Date: 2020-12-23 02:16:59.709135

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9be854994aac'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('environment',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('location', sa.String(length=100, collation='utf8_general_ci'), nullable=False),
    sa.Column('capacity', sa.Integer(), nullable=False),
    sa.Column('type', sa.String(length=50, collation='utf8_general_ci'), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(length=20, collation='utf8_general_ci'), nullable=False),
    sa.Column('last_name', sa.String(length=20, collation='utf8_general_ci'), nullable=False),
    sa.Column('password', sa.String(length=100, collation='utf8_general_ci'), nullable=False),
    sa.Column('email', sa.String(length=100, collation='utf8_general_ci'), nullable=False),
    sa.Column('tc_number', sa.String(length=11, collation='utf8_general_ci'), nullable=False),
    sa.Column('phone', sa.String(length=20, collation='utf8_general_ci'), nullable=False),
    sa.Column('type', sa.String(length=10, collation='utf8_general_ci'), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('fixture',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100, collation='utf8_general_ci'), nullable=False),
    sa.Column('type', sa.String(length=50, collation='utf8_general_ci'), nullable=False),
    sa.Column('description', sa.String(length=250, collation='utf8_general_ci'), nullable=False),
    sa.Column('size', sa.String(length=50, collation='utf8_general_ci'), nullable=False),
    sa.Column('environment_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['environment_id'], ['environment.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user_staff',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('staff_id', sa.String(length=12, collation='utf8_general_ci'), nullable=False),
    sa.ForeignKeyConstraint(['id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('staff_id')
    )
    op.create_table('user_student',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('student_id', sa.String(length=12, collation='utf8_general_ci'), nullable=False),
    sa.ForeignKeyConstraint(['id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('student_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_student')
    op.drop_table('user_staff')
    op.drop_table('fixture')
    op.drop_table('user')
    op.drop_table('environment')
    # ### end Alembic commands ###
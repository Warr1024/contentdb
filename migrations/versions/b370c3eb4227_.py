"""empty message

Revision ID: b370c3eb4227
Revises: c5e4213721dd
Create Date: 2020-07-17 19:22:15.267179

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy import orm
from app.models import ContentWarning


# revision identifiers, used by Alembic.
revision = 'b370c3eb4227'
down_revision = 'c5e4213721dd'
branch_labels = None
depends_on = None


def upgrade():
	# ### commands auto generated by Alembic - please adjust! ###
	op.create_table('content_warning',
	sa.Column('id', sa.Integer(), nullable=False),
	sa.Column('name', sa.String(length=100), nullable=False),
	sa.Column('title', sa.String(length=100), nullable=False),
	sa.Column('description', sa.String(length=500), nullable=False),
	sa.PrimaryKeyConstraint('id'),
	sa.UniqueConstraint('name')
	)
	op.create_table('content_warnings',
	sa.Column('content_warning_id', sa.Integer(), nullable=False),
	sa.Column('package_id', sa.Integer(), nullable=False),
	sa.ForeignKeyConstraint(['content_warning_id'], ['content_warning.id'], ),
	sa.ForeignKeyConstraint(['package_id'], ['package.id'], ),
	sa.PrimaryKeyConstraint('content_warning_id', 'package_id')
	)

	bind = op.get_bind()
	session = orm.Session(bind=bind)

	session.add(ContentWarning("Violence", "Non-cartoon violence"))
	session.add(ContentWarning("Drugs", "Drugs or alcohol"))
	session.add(ContentWarning("Bad Language"))
	session.add(ContentWarning("Gambling"))
	session.add(ContentWarning("Horror"))
	session.commit()

	# ### end Alembic commands ###


def downgrade():
	# ### commands auto generated by Alembic - please adjust! ###
	op.drop_table('content_warnings')
	op.drop_table('content_warning')
	# ### end Alembic commands ###

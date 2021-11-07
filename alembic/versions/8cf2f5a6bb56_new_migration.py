"""New migration

Revision ID: 8cf2f5a6bb56
Revises: 
Create Date: 2021-11-07 23:49:30.889552

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8cf2f5a6bb56'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('comercio',
    sa.Column('id', sa.BigInteger(), autoincrement=True, nullable=False),
    sa.Column('uuid', sa.String(length=36), nullable=True),
    sa.Column('nombre', sa.String(length=100), nullable=True),
    sa.Column('activo', sa.Boolean(), nullable=True),
    sa.Column('email_contacto', sa.String(length=50), nullable=True),
    sa.Column('telefono_contacto', sa.String(length=15), nullable=True),
    sa.Column('api_key', sa.String(length=36), nullable=True),
    sa.Column('fecha_creacion', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('api_key'),
    sa.UniqueConstraint('uuid')
    )
    op.create_table('empleado',
    sa.Column('id', sa.BigInteger(), autoincrement=True, nullable=False),
    sa.Column('uuid', sa.String(length=36), nullable=True),
    sa.Column('nombre', sa.String(length=40), nullable=True),
    sa.Column('apellidos', sa.String(length=40), nullable=True),
    sa.Column('pin', sa.String(length=6), nullable=True),
    sa.Column('comercio', sa.BigInteger(), nullable=True),
    sa.Column('fecha_creacion', sa.DateTime(), nullable=True),
    sa.Column('activo', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['comercio'], ['comercio.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('uuid')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('empleado')
    op.drop_table('comercio')
    # ### end Alembic commands ###
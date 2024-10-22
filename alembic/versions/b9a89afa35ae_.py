"""empty message

Revision ID: b9a89afa35ae
Revises: 4d9c948e0ed8
Create Date: 2024-10-23 02:14:57.639656

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b9a89afa35ae'
down_revision: Union[str, None] = '4d9c948e0ed8'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('messages', sa.Column('content', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('messages', 'content')
    # ### end Alembic commands ###

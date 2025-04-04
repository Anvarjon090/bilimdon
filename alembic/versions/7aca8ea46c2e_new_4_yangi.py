"""new 4 yangi 

Revision ID: 7aca8ea46c2e
Revises: 42ff02145391
Create Date: 2025-04-04 19:10:28.375074

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7aca8ea46c2e'
down_revision: Union[str, None] = '42ff02145391'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('games_owner_id_fkey', 'games', type_='foreignkey')
    op.drop_column('games', 'owner_id')
    op.drop_column('games', 'topic_id')
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('games', sa.Column('topic_id', sa.INTEGER(), autoincrement=False, nullable=False))
    op.add_column('games', sa.Column('owner_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.create_foreign_key('games_owner_id_fkey', 'games', 'users', ['owner_id'], ['id'])
    # ### end Alembic commands ###

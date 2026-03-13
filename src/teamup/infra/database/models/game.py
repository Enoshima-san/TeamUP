```python
from uuid import uuid4
from sqlalchemy import UUID, Column, LargeBinary, String
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

from .base import Base


class GameORM(Base):
    """
    Database model for a game.
    
    Attributes:
    ----------
    game_id : UUID
        Unique identifier for the game.
    game_name : str
        Name of the game.
    game_icon : bytes
        Icon for the game.
    
    Relationships:
    -------------
    user_games : UserGamesORM
        Games played by users.
    announcement : AnnouncementORM
        Announcement for the game.
    rank : RankORM
        Rank for the game.
    player_rating : PlayerRatingORM
        Player rating for the game.
    """

    __tablename__ = "game"

    # Unique identifier for the game
    game_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    # Name of the game
    game_name = Column(String(100), nullable=False)
    # Icon for the game
    game_icon = Column(LargeBinary, nullable=False)

    # Games played by users
    user_games = relationship("UserGamesORM", back_populates="game")
    # Announcement for the game
    announcement = relationship("AnnouncementORM", back_populates="game")
    # Rank for the game
    rank = relationship("RankORM", back_populates="game")
    # Player rating for the game
    player_rating = relationship("PlayerRatingORM")
```
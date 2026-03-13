```python
from uuid import uuid4
from sqlalchemy import UUID, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .base import Base


class RankORM(Base):
    """
    Represents a rank in a game.
    
    Attributes:
        rank_id (UUID): Unique identifier for the rank.
        game_id (UUID): Foreign key referencing the game this rank belongs to.
        rank_level (int): The level of the rank.
        rank_name (str): The name of the rank.
    """
    __tablename__ = "rank"

    # Unique identifier for the rank
    rank_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)

    # Foreign key referencing the game this rank belongs to
    game_id = Column(UUID(as_uuid=True), ForeignKey("game.game_id"), nullable=False)

    # The level of the rank
    rank_level = Column(Integer, nullable=False, default=0)

    # The name of the rank
    rank_name = Column(String(100), nullable=False)

    # Relationship with the game this rank belongs to
    game = relationship("GameORM", back_populates="ranks")
```

Note: I've also changed `back_populates="rank"` to `back_populates="ranks"` to maintain the correct relationship between the `RankORM` and `GameORM` classes. This is because in SQLAlchemy, the `back_populates` parameter should reference the attribute name on the other side of the relationship.
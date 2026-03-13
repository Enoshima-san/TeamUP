```python
from dataclasses import dataclass, field
from datetime import datetime
from uuid import UUID, uuid4

from ..enums import PlayersBehavior


@dataclass
class PlayerRating:
    """
    Represents a player's rating in a game.

    Attributes:
        user_id (UUID): Unique identifier of the player.
        game_id (UUID): Unique identifier of the game.
        response_id (UUID): Unique identifier of the game response.
        rating_id (UUID): Unique identifier of the rating (auto-generated).
        rating_value (int): The player's rating (default: maximum rating).
        created_at (datetime): Timestamp when the rating was created (auto-generated).
    """

    user_id: UUID
    game_id: UUID
    response_id: UUID
    rating_id: UUID = field(default_factory=uuid4)

    rating_value: int = PlayersBehavior.MAX_RATING.value
    created_at: datetime = field(default_factory=datetime.now)

    def set_rating(self, rating_value: int) -> None:
        """
        Sets the player's rating.

        Args:
            rating_value (int): The new rating value.

        Raises:
            ValueError: If the rating value is outside the valid range.
        """
        if rating_value < PlayersBehavior.MIN_RATING.value:
            raise ValueError("Rating value cannot be less than the minimum")
        if rating_value > PlayersBehavior.MAX_RATING.value:
            raise ValueError("Rating value cannot be greater than the maximum")
        self.rating_value = rating_value

    @staticmethod
    def create(
        user_id: UUID, game_id: UUID, response_id: UUID, rating_value: int = 50
    ) -> "PlayerRating":
        """
        Creates a new player rating instance.

        Args:
            user_id (UUID): Unique identifier of the player.
            game_id (UUID): Unique identifier of the game.
            response_id (UUID): Unique identifier of the game response.
            rating_value (int): The initial rating value (default: 50).

        Returns:
            PlayerRating: A new player rating instance.

        Raises:
            ValueError: If the rating value is outside the valid range.
        """
        if rating_value < PlayersBehavior.MIN_RATING.value:
            raise ValueError("Rating value cannot be less than the minimum")
        if rating_value > PlayersBehavior.MAX_RATING.value:
            raise ValueError("Rating value cannot be greater than the maximum")
        return PlayerRating(user_id, game_id, response_id, rating_value=rating_value)
```
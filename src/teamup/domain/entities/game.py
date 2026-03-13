```python
from dataclasses import dataclass, field
from typing import List
from uuid import UUID, uuid4

from .announcement import Announcement
from .player_rating import PlayerRating
from .rank import Rank
from .user_games import UserGames


@dataclass
class Game:
    """
    Represents a game with its name, icon, and associated data.
    """
    game_name: str
    """The name of the game."""
    icon: bytes
    """The icon of the game."""
    game_id: UUID = field(default_factory=uuid4)
    """A unique identifier for the game."""

    announcements: List["Announcement"] = field(default_factory=list)
    """List of announcements associated with the game."""
    ranks: List["Rank"] = field(default_factory=list)
    """List of ranks associated with the game."""
    user_games: List["UserGames"] = field(default_factory=list)
    """List of user games associated with the game."""
    player_ratings: List["PlayerRating"] = field(default_factory=list)
    """List of player ratings associated with the game."""

    def set_game_name(self, game_name: str) -> None:
        """
        Sets the name of the game.

        Args:
            game_name (str): The new name of the game.

        Raises:
            ValueError: If the game name is too short or too long.
        """
        if not (3 <= len(game_name) <= 50):
            raise ValueError("Game name must be between 3 and 50 characters")

        self.game_name = game_name

    def set_icon(self, icon: bytes) -> None:
        """
        Sets the icon of the game.

        Args:
            icon (bytes): The new icon of the game.

        Raises:
            ValueError: If the icon is empty.
        """
        if not icon:
            raise ValueError("Game icon cannot be empty")

        self.icon = icon

    @staticmethod
    def create(
        game_name: str,
        icon: bytes,
    ) -> "Game":
        """
        Creates a new game instance.

        Args:
            game_name (str): The name of the game.
            icon (bytes): The icon of the game.

        Returns:
            Game: A new game instance.

        Raises:
            ValueError: If the game name is too short or too long, or if the icon is empty.
        """
        if not (3 <= len(game_name) <= 50):
            raise ValueError("Game name must be between 3 and 50 characters")
        if not icon:
            raise ValueError("Game icon cannot be empty")

        return Game(game_name=game_name, icon=icon)
```
```python
from domain import Game
from rank import RankMapper
from ..models import GameORM
from .announcement import AnnouncementMapper
from .player_rating import PlayerRatingMapper
from .user_games import UserGamesMapper


class GameMapper:
    """
    Mapper class for converting between Game domain objects and GameORM database objects.
    """

    @staticmethod
    def to_domain(orm: GameORM | None) -> "Game":
        """
        Converts a GameORM object to a Game domain object.

        Args:
            orm: The GameORM object to convert.

        Returns:
            The converted Game domain object.

        Raises:
            ValueError: If the orm object is None.
        """
        if not orm:
            raise ValueError("ORM object is None")

        # Convert related objects to their domain representations
        user_games = UserGamesMapper.to_domain(orm.user_games) if orm.user_games else []
        announcements = AnnouncementMapper.to_domain(orm.announcements) if orm.announcements else []
        ranks = RankMapper.to_domain(orm.ranks) if orm.ranks else []
        player_ratings = PlayerRatingMapper.to_domain(orm.ratings) if orm.ratings else []

        # Create and return the Game domain object
        return Game(
            game_name=orm.game_name,  # type: ignore[reportAttributeAccessIssue]
            icon=orm.icon,  # type: ignore[reportAttributeAccessIssue]
            user_games=user_games,
            announcements=announcements,
            ranks=ranks,
            player_ratings=player_ratings,
        )

    @staticmethod
    def to_orm(entity: Game | None) -> "GameORM":
        """
        Converts a Game domain object to a GameORM object.

        Args:
            entity: The Game domain object to convert.

        Returns:
            The converted GameORM object.

        Raises:
            ValueError: If the entity object is None.
        """
        if not entity:
            raise ValueError("Entity is None")

        # Create and return the GameORM object
        return GameORM(
            game_name=entity.game_name,
            icon=entity.icon,
        )
```
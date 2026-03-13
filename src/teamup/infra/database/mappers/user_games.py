```python
from src.teamup.domain import UserGames
from ..models import UserGamesORM

class UserGamesMapper:
    """
    Mapper class for converting between UserGames domain objects and UserGamesORM database models.
    """

    @staticmethod
    def to_domain(orm: UserGamesORM | None) -> UserGames:
        """
        Converts a UserGamesORM database model to a UserGames domain object.

        Args:
            orm: The UserGamesORM database model to convert.

        Returns:
            The converted UserGames domain object.

        Raises:
            ValueError: If the ORM object is None.
        """
        if not orm:
            raise ValueError("ORM object is None")

        return UserGames(
            user_id=orm.user_id,  # type: ignore[reportArgumentType]
            game_id=orm.game_id,  # type: ignore[reportArgumentType]
            preferred=orm.preferred,  # type: ignore[reportArgumentType]
        )

    @staticmethod
    def to_orm(entity: UserGames | None) -> UserGamesORM:
        """
        Converts a UserGames domain object to a UserGamesORM database model.

        Args:
            entity: The UserGames domain object to convert.

        Returns:
            The converted UserGamesORM database model.

        Raises:
            ValueError: If the entity is None.
        """
        if not entity:
            raise ValueError("Entity is None")

        return UserGamesORM(
            user_id=entity.user_id,
            game_id=entity.game_id,
            preferred=entity.preferred,
        )
```
from domain import UserGames

from ..models import UserGamesORM


class UserGamesMapper:
    @staticmethod
    def to_domain(orm: UserGamesORM | None) -> UserGames:
        if not orm:
            raise ValueError("ORM object is None")

        return UserGames(
            user_id=orm.user_id,  # type: ignore[reportArgumentType]
            game_id=orm.game_id,  # type: ignore[reportArgumentType]
            preferred=orm.preferred,  # type: ignore[reportArgumentType]
        )

    @staticmethod
    def to_orm(entity: UserGames | None) -> UserGamesORM:
        if not entity:
            raise ValueError("Entity is None")

        return UserGamesORM(
            user_id=entity.user_id,
            game_id=entity.game_id,
            preferred=entity.preferred,
        )

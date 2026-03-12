from src.teamup.domain import PlayerRating

from ..models import PlayerRatingORM


class PlayerRatingMapper:
    @staticmethod
    def to_domain(orm: PlayerRatingORM | None) -> PlayerRating:
        if not orm:
            raise ValueError("ORM object is None")

        return PlayerRating(
            raiting_id=orm.raiting_id,  # type: ignore[reportAttributeAccessIssue]
            user_id=orm.user_id,  # type: ignore[reportArgumentType]
            game_id=orm.game_id,  # type: ignore[reportArgumentType]
            response_id=orm.response_id,  # type: ignore[reportArgumentType]
            rating_value=orm.rating_value,  # type: ignore[reportArgumentType]
            created_at=orm.created_at,  # type: ignore[reportArgumentType]
        )

    @staticmethod
    def to_orm(entity: PlayerRating | None) -> PlayerRatingORM:
        if not entity:
            raise ValueError("Entity is None")

        return PlayerRatingORM(
            raiting_id=entity.raiting_id,
            user_id=entity.user_id,
            game_id=entity.game_id,
            response_id=entity.response_id,
            raiting_value=entity.rating_value,
            created_at=entity.created_at,
        )

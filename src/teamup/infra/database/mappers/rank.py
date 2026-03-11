from domain import Rank

from ..models import RankORM


class RankMapper:
    @staticmethod
    def to_domain(orm: RankORM | None) -> "Rank":
        if not orm:
            ValueError("RankORM is None")

        return Rank(
            game_id=orm.game_id,  # type: ignore[reportArgumentType]
            rank_name=orm.rank_name,  # type: ignore[reportArgumentType]
            rank_level=orm.rank_level,  # type: ignore[reportArgumentType]
        )

    @staticmethod
    def to_orm(entity: Rank | None) -> "RankORM":
        if not entity:
            raise ValueError("Rank is None")

        return RankORM(
            game_id=entity.game_id,
            rank_name=entity.rank_name,
            rank_level=entity.rank_level,
        )

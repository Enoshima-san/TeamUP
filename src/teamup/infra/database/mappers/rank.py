```python
from domain import Rank
from ..models import RankORM

class RankMapper:
    """
    Mapper class responsible for converting between Rank domain model and RankORM model.
    """

    @staticmethod
    def to_domain(orm: RankORM | None) -> Rank:
        """
        Converts RankORM model to Rank domain model.

        Args:
            orm: RankORM model to convert.

        Returns:
            Rank domain model.

        Raises:
            ValueError: If orm is None.
        """
        if not orm:
            raise ValueError("RankORM cannot be None")

        return Rank(
            game_id=orm.game_id,  # type: ignore[reportArgumentType]
            rank_name=orm.rank_name,  # type: ignore[reportArgumentType]
            rank_level=orm.rank_level,  # type: ignore[reportArgumentType]
        )

    @staticmethod
    def to_orm(entity: Rank | None) -> RankORM:
        """
        Converts Rank domain model to RankORM model.

        Args:
            entity: Rank domain model to convert.

        Returns:
            RankORM model.

        Raises:
            ValueError: If entity is None.
        """
        if not entity:
            raise ValueError("Rank cannot be None")

        return RankORM(
            game_id=entity.game_id,
            rank_name=entity.rank_name,
            rank_level=entity.rank_level,
        )
```
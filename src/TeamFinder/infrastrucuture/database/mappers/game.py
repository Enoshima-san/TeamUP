from domain import Game
from rank import RankMapper

from ..models import GameORM
from .announcement import AnnouncementMapper
from .player_rating import PlayerRatingMapper
from .user_games import UserGamesMapper


class GameMapper:
    @staticmethod
    def to_domain(orm: GameORM | None) -> "Game":
        if not orm:
            raise ValueError("ORM object is None")

        user_games = [UserGamesMapper.to_domain(ug) for ug in orm.user_games]
        announcements = [AnnouncementMapper.to_domain(a) for a in orm.announcements]
        ranks = [RankMapper.to_domain(r) for r in orm.ranks]
        player_ratings = [PlayerRatingMapper.to_domain(pr) for pr in orm.ratings]

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
        if not entity:
            raise ValueError("Entity is None")

        return GameORM(
            game_name=entity.game_name,
            icon=entity.icon,
        )

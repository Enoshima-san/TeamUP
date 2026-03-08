from domain import User

from ..models import UserORM
from .announcement import AnnouncementMapper
from .complaints import ComplaintsMapper
from .player_rating import PlayerRatingMapper
from .response import ResponseMapper
from .user_games import UserGamesMapper


class UserMapper:
    @staticmethod
    def to_domain(orm: UserORM | None) -> User:
        if not orm:
            raise ValueError("ORM object is None")

        user_games = [UserGamesMapper.to_domain(ug) for ug in orm.user_games]
        user_ratings = [PlayerRatingMapper.to_domain(r) for r in orm.ratings]
        user_responses = [ResponseMapper.to_domain(r) for r in orm.responses]
        user_announcements = [
            AnnouncementMapper.to_domain(a) for a in orm.announcements
        ]
        user_complaints = [ComplaintsMapper.to_domain(c) for c in orm.complaints]

        return User(
            user_id=orm.user_id,  # type: ignore[reportArgumentType]
            username=orm.username,  # type: ignore[reportArgumentType]
            email=orm.email,  # type: ignore[reportArgumentType]
            password_hash=orm.password_hash,  # type: ignore[reportArgumentType]
            age=orm.age,  # type: ignore[reportArgumentType]
            about_me=orm.about_me,  # type: ignore[reportArgumentType]
            blocked_reason=orm.blocked_reason,  # type: ignore[reportArgumentType]
            registration_date=orm.registration_date,  # type: ignore[reportArgumentType]
            last_login=orm.last_login,  # type: ignore[reportArgumentType]
            is_active=orm.is_active,  # type: ignore[reportArgumentType]
            role=orm.role,  # type: ignore[reportArgumentType]
            is_blocked=orm.is_blocked,  # type: ignore[reportArgumentType]
            user_games=user_games,
            user_raitings=user_ratings,
            user_responses=user_responses,
            user_announcements=user_announcements,
            user_complaints=user_complaints,
        )

    @staticmethod
    def to_orm(entity: User | None) -> UserORM:
        if not entity:
            raise ValueError("Entity is None")

        return UserORM(
            user_id=entity.user_id,
            username=entity.username,
            email=entity.email,
            password_hash=entity.password_hash,
            age=entity.age,
            about_me=entity.about_me,
            blocked_reason=entity.blocked_reason,
            registration_date=entity.registration_date,
            last_login=entity.last_login,
            is_active=entity.is_active,
            role=entity.role,
            is_blocked=entity.is_blocked,
        )

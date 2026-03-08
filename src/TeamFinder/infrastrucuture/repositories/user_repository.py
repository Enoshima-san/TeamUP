from uuid import UUID

from application import IUserRepository
from core import logger
from domain import User
from sqlalchemy import select
from sqlalchemy.orm import selectinload

from ..database import UserMapper, UserORM, async_session


class UserRepository(IUserRepository):
    def __init__(self):
        self.session = async_session()
        logger.info("UserRepository проинициализирован")

    async def create(self, user: User) -> User | None:
        """
        Возвращает User\n\n
        Если пользователь уже в базе, возваращает `None`,
        иначе возвращаем пустого пользователся
        """
        stmt = select(UserORM).where(
            UserORM.email == user.email and UserORM.username == user.username
        )
        result = await self.session.execute(stmt)

        already_exists_user = result.scalar()
        if not already_exists_user:
            logger.warning(
                (
                    f"Пользователь с почтой {user.email} и/или "
                    f"именем пользователя{user.username} уже существует"
                )
            )
            return None

        orm = UserMapper.to_orm(user)
        self.session.add(orm)
        await self.session.commit()
        await self.session.refresh(orm)
        logger.info(f"Пользователь с id {user.user_id} создан")

        return UserMapper.to_domain(orm)

    async def delete(self, user: int | User) -> bool:
        """Возвращает результат удаения пользователя"""
        if isinstance(user, int):
            orm_user = await self.session.get(UserORM, user)
            if not orm_user:
                logger.warning(f"Пользователь с id {user} не найден")
                return False
            await self.session.delete(orm_user)
            await self.session.commit()
            logger.info(f"Пользователь с id {user} удален")
            return True

        orm_user = await self.session.get(UserORM, user.user_id)
        if not orm_user:
            logger.warning(f"Пользователь с id {user.user_id} не найден")
            return False
        await self.session.delete(orm_user)
        await self.session.commit()
        logger.info(f"Пользователь с id {user.user_id} удален")
        return True

    async def get_by_id(self, id: UUID) -> User | None:
        """
        Возвращает User\n\n
        Если пользователь не найден, возваращаем `None`
        """
        stmt = select(UserORM).options(
            selectinload(UserORM.user_games),
            selectinload(UserORM.ratings),
            selectinload(UserORM.responses),
            selectinload(UserORM.announcements),
            selectinload(UserORM.complaints),
        )
        result = await self.session.execute(stmt)
        user = result.scalar()

        if not user:
            logger.warning(f"Пользователь с id {id} не найден")
            return None

        return UserMapper.to_domain(user)

    async def get_by_email(self, email: str) -> User | None:
        """
        Возвращает User\n\n
        Если пользователь не найден, возваращаем `None`
        """
        stmt = select(UserORM).where(UserORM.email == email)
        result = await self.session.execute(stmt)
        user = result.scalar()

        if not user:
            logger.warning(f"Пользователь с email {email} не найден")
            return None

        return UserMapper.to_domain(user)

    async def get_by_username(self, username: str) -> User | None:
        """
        Возвращает User\n\n
        Если пользователь не найден, возваращаем `None`
        """
        stmt = select(UserORM).where(UserORM.username == username)
        result = await self.session.execute(stmt)
        user = result.scalar()

        if not user:
            logger.warning(f"Пользователь с username {username} не найден")
            return None

        return UserMapper.to_domain(user)

    async def get_all(self) -> list[User]:
        """
        Возвращает User\n\n
        Если пользователь не найден, возваращаем `None`
        """
        stmt = select(UserORM)
        result = await self.session.execute(stmt)
        users = result.scalars().all()

        return [UserMapper.to_domain(user) for user in users]

    async def update(self, user: User) -> User | None:
        """
        Обновляет пользователя в базе данных\n\n
        Если пользователь не найден, возваращаем `None`
        """
        stmt = select(UserORM).where(UserORM.user_id == user.user_id)
        result = await self.session.execute(stmt)
        orm_user = result.scalar()

        if not orm_user:
            logger.warning(f"Пользователь с id {user.user_id} не найден")
            return None

        orm_user.username = user.username  # type: ignore[reportAttributeAccessIssue]
        orm_user.email = user.email  # type: ignore[reportAttributeAccessIssue]
        orm_user.password_hash = user.password_hash  # type: ignore[reportAttributeAccessIssue]
        orm_user.registration_date = user.registration_date  # type: ignore[reportAttributeAccessIssue]
        orm_user.last_login = user.last_login  # type: ignore[reportAttributeAccessIssue]
        orm_user.is_active = user.is_active  # type: ignore[reportAttributeAccessIssue]
        orm_user.role = user.role  # type: ignore[reportAttributeAccessIssue]
        orm_user.has_microphone = user.has_microphone  # type: ignore[reportAttributeAccessIssue]
        orm_user.age = user.age  # type: ignore[reportAttributeAccessIssue]
        orm_user.about_me = user.about_me  # type: ignore[reportAttributeAccessIssue]
        orm_user.is_blocked = user.is_blocked  # type: ignore[reportAttributeAccessIssue]
        orm_user.blocked_reason = user.blocked_reason  # type: ignore[reportAttributeAccessIssue]

        await self.session.commit()
        await self.session.refresh(orm_user)

        return UserMapper.to_domain(orm_user)

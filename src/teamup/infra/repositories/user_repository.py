```python
from typing import Union
from uuid import UUID
from sqlalchemy import or_, select
from sqlalchemy.orm import selectinload
from src.teamup.application import IUserRepository
from src.teamup.core import logger
from src.teamup.domain import User
from ..database import UserMapper, UserORM, async_session


class UserRepository(IUserRepository):
    """
    Repository class for managing user data.
    """

    def __init__(self):
        """
        Initializes the repository with an async session.
        """
        self.session = async_session()
        logger.info("UserRepository initialized")

    async def create_user(self, user: User) -> User | None:
        """
        Creates a new user in the database.

        Args:
        user (User): The user to be created.

        Returns:
        User | None: The created user if the user already exists, otherwise None.
        """
        # Check if the user already exists
        stmt = select(UserORM).where(
            UserORM.email == user.email and UserORM.username == user.username
        )
        result = await self.session.execute(stmt)
        already_exists_user = result.scalar()
        if already_exists_user:
            logger.warning(
                (
                    f"User with email {user.email} and/or username {user.username} already exists"
                )
            )
            return None

        # Create a new ORM object from the user
        orm = UserMapper.to_orm(user)
        self.session.add(orm)
        await self.session.commit()
        await self.session.refresh(orm)
        logger.info(f"User with id {user.user_id} created")

        return UserMapper.to_domain(orm)

    async def delete_user(self, user_id: int | User) -> bool:
        """
        Deletes a user from the database.

        Args:
        user_id (int | User): The ID of the user to be deleted.

        Returns:
        bool: True if the user was deleted successfully, False otherwise.
        """
        if isinstance(user_id, int):
            # Get the ORM object from the database
            orm_user = await self.session.get(UserORM, user_id)
            if not orm_user:
                logger.warning(f"User with id {user_id} not found")
                return False
            await self.session.delete(orm_user)
            await self.session.commit()
            logger.info(f"User with id {user_id} deleted")
            return True

        # Get the ORM object from the database
        orm_user = await self.session.get(UserORM, user_id.user_id)
        if not orm_user:
            logger.warning(f"User with id {user_id.user_id} not found")
            return False
        await self.session.delete(orm_user)
        await self.session.commit()
        logger.info(f"User with id {user_id.user_id} deleted")
        return True

    async def get_user_by_id(self, id: UUID) -> User | None:
        """
        Retrieves a user by their ID.

        Args:
        id (UUID): The ID of the user to be retrieved.

        Returns:
        User | None: The user if found, otherwise None.
        """
        # Load related objects
        stmt = select(UserORM).options(
            selectinload(UserORM.user_games),
            selectinload(UserORM.player_rating),
            selectinload(UserORM.response),
            selectinload(UserORM.announcement),
            selectinload(UserORM.complaints),
        )
        result = await self.session.execute(stmt)
        user = result.scalar()

        if not user:
            logger.warning(f"User with id {id} not found")
            return None

        return UserMapper.to_domain(user)

    async def check_new_user(self, email: str, username: str) -> bool:
        """
        Checks if a user with the given email and username exists.

        Args:
        email (str): The email of the user to be checked.
        username (str): The username of the user to be checked.

        Returns:
        bool: True if the user does not exist, False otherwise.
        """
        # Check if the user already exists
        stmt = select(UserORM).where(
            or_(UserORM.email == email, UserORM.username == username)
        )
        result = await self.session.execute(stmt)

        return result.scalar() is None

    async def get_user_by_email(self, email: str) -> User | None:
        """
        Retrieves a user by their email.

        Args:
        email (str): The email of the user to be retrieved.

        Returns:
        User | None: The user if found, otherwise None.
        """
        # Get the ORM object from the database
        stmt = select(UserORM).where(UserORM.email == email)
        result = await self.session.execute(stmt)
        user = result.scalar()

        if not user:
            logger.warning(f"User with email {email} not found")
            return None

        return UserMapper.to_domain(user)

    async def get_user_by_username(self, username: str) -> User | None:
        """
        Retrieves a user by their username.

        Args:
        username (str): The username of the user to be retrieved.

        Returns:
        User | None: The user if found, otherwise None.
        """
        # Get the ORM object from the database
        stmt = select(UserORM).where(UserORM.username == username)
        result = await self.session.execute(stmt)
        user = result.scalar()

        if not user:
            logger.warning(f"User with username {username} not found")
            return None

        return UserMapper.to_domain(user)

    async def get_all_users(self) -> list[User]:
        """
        Retrieves all users.

        Returns:
        list[User]: A list of users.
        """
        # Get all ORM objects from the database
        stmt = select(UserORM)
        result = await self.session.execute(stmt)
        users = result.scalars().all()

        return [UserMapper.to_domain(user) for user in users]

    async def update_user(self, user: User) -> User | None:
        """
        Updates a user in the database.

        Args:
        user (User): The user to be updated.

        Returns:
        User | None: The updated user if found, otherwise None.
        """
        # Get the ORM object from the database
        stmt = select(UserORM).where(UserORM.user_id == user.user_id)
        result = await self.session.execute(stmt)
        orm_user = result.scalar()

        if not orm_user:
            logger.warning(f"User with id {user.user_id} not found")
            return None

        # Update the ORM object
        orm_user.username = user.username
        orm_user.email = user.email
        orm_user.password_hash = user.password_hash
        orm_user.registration_date = user.registration_date
        orm_user.last_login = user.last_login
        orm_user.is_active = user.is_active
        orm_user.role = user.role
        orm_user.has_microphone = user.has_microphone
        orm_user.age = user.age
        orm_user.about_me = user.about_me
        orm_user.is_blocked = user.is_blocked
        orm_user.blocked_reason = user.blocked_reason

        await self.session.commit()
        await self.session.refresh(orm_user)

        return UserMapper.to_domain(orm_user)
```
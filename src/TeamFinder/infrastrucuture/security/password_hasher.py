from passlib.context import CryptContext


class PasswordHasher:
    _context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    @staticmethod
    def hash(password: str) -> str:
        return PasswordHasher._context.hash(password)

    @staticmethod
    def verify(password: str, hashed: str) -> bool:
        return PasswordHasher._context.verify(password, hashed)

from enum import Enum


class AnnouncementStatus(str, Enum):
    ACTIVE = "активный"
    PAUSED = "приостановлен"
    COMPLETED = "завершен"


class ResponseStatus(str, Enum):
    PENDING = "рассматривается"
    DECLINED = "отклонен"
    ACCEPTED = "принят"


class ComplaintStatus(str, Enum):
    OPEN = "открыт"
    RESOLVED = "решен"
    DECLINED = "отклонен"


class UserRole(str, Enum):
    ADMIN = "admin"
    USER = "user"

from dataclasses import dataclass, field
from datetime import datetime
from typing import List, Optional
from uuid import UUID, uuid4

from ..enums import AnnouncementStatus
from .complaints import Complaints


@dataclass
class Announcement:
    user_id: UUID
    game_id: UUID
    announcement_id: UUID = field(default_factory=uuid4)

    type: Optional[str] = None
    rank_min: Optional[int] = None
    rank_max: Optional[int] = None
    description: Optional[str] = None
    status: str = AnnouncementStatus.ACTIVE.value
    created_at: datetime = field(default_factory=datetime.now)
    updated_at: datetime = field(default_factory=datetime.now)

    announcement_complaints: List["Complaints"] = field(default_factory=list)

    def start(self):
        """
        Принудительный запуск ананонса
        """
        if self.status == AnnouncementStatus.ACTIVE.value:
            raise ValueError("Анонс уже активен!")
        if self.status == AnnouncementStatus.PAUSED.value:
            raise ValueError("Анонс уже приостановлен!")
        if self.status == AnnouncementStatus.COMPLETED.value:
            raise ValueError("Анонс уже завершён!")
        self.status = AnnouncementStatus.ACTIVE.value
        self.updated_at = datetime.now()

    def pause(self):
        if self.status == AnnouncementStatus.COMPLETED:
            raise ValueError("Невозможно приостановить завершённый анонс!")
        self.status = AnnouncementStatus.PAUSED
        self.updated_at = datetime.now()

    def complete(self):
        if self.status == AnnouncementStatus.COMPLETED.value:
            raise ValueError("Анонс уже завершён!")
        self.status = AnnouncementStatus.COMPLETED.value
        self.updated_at = datetime.now()

    def is_active(self) -> bool:
        return self.status == AnnouncementStatus.ACTIVE.value

    def set_description(self, description: str):
        self.description = description
        self.updated_at = datetime.now()

    def set_ranks(self, min_rank: int | None = None, max_rank: int | None = None):
        self.rank_min = min_rank
        self.rank_max = max_rank
        self.updated_at = datetime.now()

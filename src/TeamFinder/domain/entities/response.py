from dataclasses import dataclass, field
from datetime import datetime
from typing import List
from uuid import UUID, uuid4

from ..enums import ResponseStatus
from .complaints import Complaints


@dataclass
class Response:
    announcement_id: UUID
    user_id: UUID
    response_id: UUID = field(default_factory=uuid4)
    status: str = ResponseStatus.PENDING.value
    created_at: datetime = field(default_factory=datetime.now)
    updated_at: datetime = field(default_factory=datetime.now)

    response_complaints: List["Complaints"] = field(default_factory=list)

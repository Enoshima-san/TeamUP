from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional
from uuid import UUID, uuid4

from ..enums import ComplaintStatus


@dataclass
class Complaints:
    user_id: UUID
    announcement_id: UUID
    response_id: UUID
    complaint_id: UUID = field(default_factory=uuid4)

    status: str = ComplaintStatus.OPEN.value
    created_at: datetime = field(default_factory=datetime.now)
    resolved_at: Optional[datetime] = field(default_factory=datetime.now)

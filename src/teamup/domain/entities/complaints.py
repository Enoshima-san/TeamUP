```python
from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional
from uuid import UUID, uuid4

from ..enums import ComplaintStatus


@dataclass
class Complaint:
    """
    Represents a complaint with its attributes and methods.
    """

    user_id: UUID
    announcement_id: UUID
    response_id: UUID
    complaint_id: UUID = field(default_factory=uuid4)

    status: str = ComplaintStatus.OPEN.value
    created_at: datetime = field(default_factory=datetime.now)
    resolved_at: Optional[datetime] = field(default_factory=datetime.now)

    def set_status(self, status: str) -> None:
        """
        Sets the status of the complaint.

        Args:
            status: The new status of the complaint (e.g., ComplaintStatus.OPEN.value).
        """
        self.status = status

    def resolve(self) -> None:
        """
        Resolves the complaint by setting its status to RESOLVED and updating the resolved_at timestamp.
        """
        self.status = ComplaintStatus.RESOLVED.value
        self.resolved_at = datetime.now()

    @staticmethod
    def create(
        user_id: UUID,
        announcement_id: UUID,
        response_id: UUID,
        status: str = ComplaintStatus.OPEN.value,
        created_at: datetime = datetime.now(),
        resolved_at: datetime = datetime.now(),
    ) -> "Complaint":
        """
        Creates a new Complaint instance.

        Args:
            user_id: The ID of the user who made the complaint.
            announcement_id: The ID of the announcement related to the complaint.
            response_id: The ID of the response related to the complaint.
            status: The initial status of the complaint (default: ComplaintStatus.OPEN.value).
            created_at: The timestamp when the complaint was created (default: current time).
            resolved_at: The timestamp when the complaint was resolved (default: current time).

        Returns:
            A new Complaint instance.
        """
        return Complaint(
            user_id=user_id,
            announcement_id=announcement_id,
            response_id=response_id,
            status=status,
            created_at=created_at,
            resolved_at=resolved_at,
        )
```
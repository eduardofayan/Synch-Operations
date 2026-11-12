from datetime import datetime

from sqlalchemy import String
from sqlalchemy import DateTime
from sqlalchemy import ForeignKey

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from app.database.base import Base


class QueueItem(Base):

    __tablename__ = "queue_items"

    id: Mapped[int] = mapped_column(
        primary_key=True
    )

    automation_id: Mapped[int] = mapped_column(
        ForeignKey("automations.id")
    )

    status: Mapped[str] = mapped_column(
        String(50),
        default="pending"
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow
    )
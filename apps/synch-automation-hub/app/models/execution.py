from datetime import datetime

from sqlalchemy import String
from sqlalchemy import DateTime
from sqlalchemy import ForeignKey

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from app.database.base import Base


class Execution(Base):

    __tablename__ = "executions"

    id: Mapped[int] = mapped_column(
        primary_key=True
    )

    queue_item_id: Mapped[int] = mapped_column(
        ForeignKey("queue_items.id")
    )

    agent_id: Mapped[int] = mapped_column(
        ForeignKey("agents.id")
    )

    status: Mapped[str] = mapped_column(
        String(30)
    )

    started_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow
    )

    finished_at: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=True
    )
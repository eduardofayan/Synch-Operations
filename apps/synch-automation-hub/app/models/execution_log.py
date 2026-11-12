from datetime import datetime

from sqlalchemy import String
from sqlalchemy import Text
from sqlalchemy import DateTime
from sqlalchemy import ForeignKey

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from app.database.base import Base


class ExecutionLog(Base):

    __tablename__ = "execution_logs"

    id: Mapped[int] = mapped_column(
        primary_key=True
    )

    execution_id: Mapped[int] = mapped_column(
        ForeignKey("executions.id")
    )

    level: Mapped[str] = mapped_column(
        String(20)
    )

    message: Mapped[str] = mapped_column(
        Text
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow
    )
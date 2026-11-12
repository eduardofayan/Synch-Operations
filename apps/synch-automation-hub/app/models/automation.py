from sqlalchemy import String
from sqlalchemy import Boolean
from sqlalchemy import Text

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from app.database.base import Base

# Classe que representa uma automação no sistema
class Automation(Base):

    __tablename__ = "automations"

    id: Mapped[int] = mapped_column(
        primary_key=True
    )

    name: Mapped[str] = mapped_column(
        String(150)
    )

    description: Mapped[str] = mapped_column(
        Text,
        nullable=True
    )

    version: Mapped[str] = mapped_column(
        String(20),
        default="1.0.0"
    )

    active: Mapped[bool] = mapped_column(
        Boolean,
        default=True
    )
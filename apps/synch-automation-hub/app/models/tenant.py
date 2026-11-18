from sqlalchemy import Boolean
from sqlalchemy import String

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from app.database.base import Base

""" Modelo que representa um inquilino (tenant) no sistema.
    Descrição: Representa um inquilino (tenant) no sistema, contendo informações como nome e status de atividade.
"""

# Classe que representa um inquilino (tenant) no sistema.
class Tenant(Base):

    # Nome da tabela no banco de dados que armazena os inquilinos (tenants).
    __tablename__ = "tenants"

    # Identificador único do inquilino (tenant).
    id: Mapped[int] = mapped_column(
        primary_key=True
    )

    # Nome do inquilino (tenant).
    name: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )

    # Indica se o inquilino (tenant) está ativo no sistema.
    active: Mapped[bool] = mapped_column(
        Boolean,
        default=True
    )
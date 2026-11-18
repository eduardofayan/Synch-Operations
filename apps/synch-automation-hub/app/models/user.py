from sqlalchemy import String
from sqlalchemy import Boolean
from sqlalchemy import ForeignKey

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from app.database.base import Base

""" 
Modelo que representa um usuário no sistema.
    Descrição: Representa um usuário no sistema, contendo informações como nome, email, senha, status de atividade e papel (role).
"""

# Classe que representa um usuário no sistema
class User(Base):

    # Nome da tabela no banco de dados que armazena os usuários.
    __tablename__ = "users"

    # Identificador único do usuário.
    id: Mapped[int] = mapped_column(
        primary_key=True
    )

    # Nome do usuário.
    name: Mapped[str] = mapped_column(
        String(150),
        nullable=False
    )

    # Email do usuário.
    email: Mapped[str] = mapped_column(
        String(255),
        unique=True,
        nullable=False
    )

    # Hash da senha do usuário.
    password_hash: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )

    # Indica se o usuário está ativo no sistema.
    active: Mapped[bool] = mapped_column(
        Boolean,
        default=True
    )

    # Identificador do papel (role) associado ao usuário.
    # Chave estrangeira que referencia a tabela de papéis (roles).
    role_id: Mapped[int] = mapped_column(
        ForeignKey("roles.id")
    )

    # Relacionamento com a tabela de papéis (roles).
    role = relationship(
        "Role"
    )
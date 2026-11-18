from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.core.config import settings
import os

# Criação do engine(Engine é o objeto que gerencia a conexão com o banco de dados e executa as operações) e da sessão do SQLAlchemy
engine = create_engine(
    settings.DATABASE_URL,
    echo=True
)

# Função para obter a sessão do banco de dados
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)
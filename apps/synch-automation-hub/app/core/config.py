from dotenv import load_dotenv
import os

load_dotenv()

# Classe de configuração do aplicativo
class Settings:
    # Nome do projeto
    PROJECT_NAME: str = "Synch Automation Hub"
    # URL de conexão com o banco de dados
    DATABASE_URL: str = os.getenv("DATABASE_URL")

# Instância da configuração do aplicativo
settings = Settings()
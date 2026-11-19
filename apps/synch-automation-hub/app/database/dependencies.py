from app.database.database import SessionLocal

# Função para obter uma sessão de banco de dados
def get_db():
    
    # Cria uma nova sessão de banco de dados
    db = SessionLocal()

    # Tenta fornecer a sessão de banco de dados para o contexto de uso
    try:
        yield db
    finally:
        db.close()
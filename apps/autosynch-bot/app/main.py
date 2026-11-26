from app.agent.worker import Worker

""" 
Função principal do aplicativo AutoSynch.
Inicializa e executa o worker responsável pelas tarefas do bot.
"""
# Define a função principal do aplicativo AutoSynch
def main():
    # Inicializa o worker responsável por executar as tarefas do bot
    worker = Worker()
    worker.start()

# Executa a função principal se o script for executado diretamente
if __name__ == "__main__":
    main()
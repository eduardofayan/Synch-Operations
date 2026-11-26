import time
from app.services.registration import RegistrationService
from app.services.heartbeat import HeartbeatService
from app.services.jobs import JobService

""" 
Worker responsável por executar as tarefas do bot AutoSynch.
"""
# Classe que representa o worker do bot AutoSynch
class Worker:

    # Inicializa o worker com o estado de execução e o ID do bot
    def __init__(self):
        self.running = True
        self.bot_id = None

    # Função que inicia o worker e executa o loop principal
    def start(self):
        print("AutoSynch Bot iniciado")
        registration = RegistrationService.register()
        self.bot_id = registration["id"]

        if registration["created"]:
            print(
                f"Novo Bot registrado. ID={self.bot_id}"
            )
        else:
            print(
                f"Bot existente encontrado. ID={self.bot_id}"
            )

        # Loop principal do worker
        while self.running:
            try:
                HeartbeatService.send(self.bot_id)
                print("Heartbeat enviado")
            except Exception as e:
                print(f"Erro no heartbeat: {e}")
                
            jobs = JobService.get_jobs(
                self.bot_id
            )

            print(
                f"{len(jobs)} jobs encontrados"
            )

            time.sleep(30)

    # Função que para o worker e encerra o loop principal
    def stop(self):
        self.running = False
        print("AutoSynch Bot parado")
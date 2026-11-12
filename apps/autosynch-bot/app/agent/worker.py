import time


class Worker:

    def __init__(self):

        self.running = True

    def start(self):

        print("AutoSynch Agent iniciado")

        while self.running:

            print("Buscando trabalhos...")

            time.sleep(30)

    def stop(self):

        self.running = False
from app.agent.worker import Worker

def main():
    worker = Worker()
    worker.start()

if __name__ == "__main__":
    main()
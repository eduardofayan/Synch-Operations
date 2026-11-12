from fastapi import FastAPI

app = FastAPI(
    title="Synch Automation Hub",
    description="Platform responsible for orchestration, scheduling and monitoring of automations.",
    version="0.1.0"
)

@app.get("/")
def root():
    return {
        "application": "Synch Automation Hub",
        "version": "0.1.0",
        "status": "running"
    }
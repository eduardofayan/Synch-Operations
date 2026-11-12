import win32serviceutil
import win32service
import win32event

from app.agent.worker import Worker

class AutoSynchService(win32serviceutil.ServiceFramework):
    _svc_name_ = "AutoSynchAgent"
    _svc_display_name_ = "AutoSynch Agent"
    _svc_description_ = (
        "Motor de execução das automações "
        "da Synch Operations."
    )

    def __init__(self, args):
        win32serviceutil.ServiceFramework.__init__(
            self,
            args
        )
        self.stop_event = win32event.CreateEvent(
            None,
            0,
            0,
            None
        )

    def SvcStop(self):
        self.ReportServiceStatus(
            win32service.SERVICE_STOP_PENDING
        )
        win32event.SetEvent(
            self.stop_event
        )

    def SvcDoRun(self):
        worker = Worker()
        worker.start()

if __name__ == "__main__":
    win32serviceutil.HandleCommandLine(
        AutoSynchService
    )
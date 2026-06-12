from datetime import datetime


class BaseRuntime:

    def __init__(self):

        self.started_at = (
            str(datetime.now())
        )

        self.runtime_status = (
            "running"
        )

    # ====================================
    # STOP
    # ====================================

    def stop(self):

        self.runtime_status = (
            "stopped"
        )
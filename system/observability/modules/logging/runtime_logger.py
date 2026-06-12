import json

from pathlib import Path

from datetime import datetime

from config.paths import BASE_DIR


class RuntimeLogger:

    def __init__(self):

        self.log_path = (

            Path(BASE_DIR) /

            "system/observability/logs/runtime_logs.json"
        )

        self.initialize_logs()

    # ========================================
    # INITIALIZE LOGS
    # ========================================

    def initialize_logs(self):

        if not self.log_path.exists():

            with open(
                self.log_path,
                "w"
            ) as f:

                json.dump([], f)

            print(
                "\nRuntime logging initialized ✅"
            )

    # ========================================
    # LOAD LOGS
    # ========================================

    def load_logs(self):

        with open(
            self.log_path,
            "r"
        ) as f:

            logs = json.load(f)

        return logs

    # ========================================
    # WRITE LOG
    # ========================================

    def log(

        self,
        subsystem,
        event,
        status,
        details=None

    ):

        logs = self.load_logs()

        entry = {

            "timestamp":
                str(datetime.now()),

            "subsystem":
                subsystem,

            "event":
                event,

            "status":
                status,

            "details":
                details
        }

        logs.append(entry)

        with open(
            self.log_path,
            "w"
        ) as f:

            json.dump(
                logs,
                f,
                indent=4
            )

        print(
            "\nRuntime event logged ✅"
        )

        return entry
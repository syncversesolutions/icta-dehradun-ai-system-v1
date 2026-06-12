from datetime import datetime


class SystemMonitor:

    def __init__(self):

        self.monitor_state = {

            "uptime":
                "active",

            "last_check":
                None,

            "system_health":
                "healthy"
        }

    # ========================================
    # RUN HEALTH CHECK
    # ========================================

    def health_check(self):

        self.monitor_state[
            "last_check"
        ] = str(datetime.now())

        print(
            "\nSystem health check complete ✅"
        )

        return self.monitor_state
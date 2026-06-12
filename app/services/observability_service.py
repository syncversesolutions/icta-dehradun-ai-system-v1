from system.observability.modules.monitoring.system_monitor import (
    SystemMonitor
)
from system.observability.modules.logging.runtime_logger import (
    RuntimeLogger
)
class ObservabilityService:
    def __init__(self):
        self.monitor = (
            SystemMonitor()
        )
        self.logger = (
            RuntimeLogger()
        )
    # ========================================
    # GET HEALTH
    # ========================================
    def get_health(self):
        return (
            self.monitor.health_check()
        )
    # ========================================
    # GET LOGS
    # ========================================
    def get_logs(self):
        return (
            self.logger.load_logs()
        )
    # ========================================
    # GET METRICS
    # ========================================
    def get_metrics(self):
        logs = (
            self.logger.load_logs()
        )
        return [
            {
                "metric":
                    "runtime_logs",
                "value":
                    len(logs)
            },
            {
                "metric":
                    "system_health",
                "value":
                    "healthy"
            }
        ]
    # ========================================
    # GET TRACES
    # ========================================
    def get_traces(self):
        logs = (
            self.logger.load_logs()
        )
        traces = []
        for log in logs:
            traces.append({
                "workflow":
                    log.get(
                        "event",
                        "unknown"
                    ),
                "stage":
                    log.get(
                        "status",
                        "unknown"
                    )
            })
        return traces
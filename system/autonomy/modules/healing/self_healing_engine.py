from datetime import datetime


class SelfHealingEngine:

    def __init__(self):

        self.healing_log = []

    # ========================================
    # DETECT FAILURE
    # ========================================

    def detect_failure(
        self,
        workflow
    ):

        status = workflow.get(
            "status",
            "unknown"
        )

        return status != "completed"

    # ========================================
    # APPLY RECOVERY
    # ========================================

    def apply_recovery(
        self,
        workflow_name
    ):

        recovery = {

            "workflow":
                workflow_name,

            "recovery":
                "restart_execution",

            "timestamp":
                str(datetime.now())
        }

        self.healing_log.append(
            recovery
        )

        print(
            "\nSelf-healing recovery applied ✅"
        )

        return recovery

    # ========================================
    # MONITOR EXECUTION LOGS
    # ========================================

    def monitor_execution(
        self,
        execution_logs
    ):

        failures = []

        for item in execution_logs:

            if item.get(
                "status"
            ) != "executed":

                failures.append(
                    item
                )

        return failures

    # ========================================
    # AUTO HEAL
    # ========================================

    def auto_heal(
        self,
        execution_logs
    ):

        failures = (

            self.monitor_execution(
                execution_logs
            )
        )

        recoveries = []

        for failure in failures:

            recovery = (

                self.apply_recovery(
                    failure.get(
                        "action",
                        "unknown"
                    )
                )
            )

            recoveries.append(
                recovery
            )

        return recoveries

    # ========================================
    # GET HEALING LOG
    # ========================================

    def get_healing_log(self):

        return self.healing_log
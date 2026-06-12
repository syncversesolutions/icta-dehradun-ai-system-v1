from datetime import datetime


class ExecutionTracer:

    def __init__(self):

        self.trace_log = []

    # ========================================
    # TRACE EXECUTION
    # ========================================

    def trace(

        self,
        workflow,
        stage

    ):

        trace = {

            "workflow":
                workflow,

            "stage":
                stage,

            "timestamp":
                str(datetime.now())
        }

        self.trace_log.append(trace)

        print(
            "\nExecution traced ✅"
        )

        return trace
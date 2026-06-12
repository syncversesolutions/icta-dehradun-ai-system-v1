from datetime import datetime


class MetricsCollector:

    def __init__(self):

        self.metrics = []

    # ========================================
    # RECORD METRIC
    # ========================================

    def record(

        self,
        metric_name,
        value

    ):

        metric = {

            "metric":
                metric_name,

            "value":
                value,

            "timestamp":
                str(datetime.now())
        }

        self.metrics.append(metric)

        print(
            "\nMetric recorded ✅"
        )

        return metric

    # ========================================
    # GET METRICS
    # ========================================

    def get_metrics(self):

        return self.metrics
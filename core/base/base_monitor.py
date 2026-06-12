class BaseMonitor:

    def __init__(self):

        self.health_status = (
            "healthy"
        )

    # ====================================
    # GET HEALTH
    # ====================================

    def health(self):

        return {

            "health":
                self.health_status
        }
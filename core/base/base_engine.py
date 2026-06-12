from datetime import datetime


class BaseEngine:

    def __init__(self):

        self.created_at = (
            str(datetime.now())
        )

        self.status = "initialized"

    # ====================================
    # STATUS
    # ====================================

    def set_status(

        self,
        status

    ):

        self.status = status

    # ====================================
    # HEALTH
    # ====================================

    def health(self):

        return {

            "status":
                self.status,

            "created_at":
                self.created_at
        }
class PredictionService:

    def __init__(self):

        pass

    # ========================================
    # GET GLOBAL PREDICTIONS
    # ========================================

    def get_predictions(self):

        return [

            {

                "forecast":
                    "traffic_surge",

                "probability":
                    0.85
            },

            {

                "forecast":
                    "crowd_pressure",

                "probability":
                    0.79
            }
        ]
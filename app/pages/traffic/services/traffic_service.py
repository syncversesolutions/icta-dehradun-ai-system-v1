import pandas as pd


class TrafficService:

    def __init__(self):

        self.prediction_path = (
            "/content/drive/MyDrive/project_cd/"
            "domains/traffic/data/predictions/"
            "traffic_predictions.csv"
        )

        self.signal_path = (
            "/content/drive/MyDrive/project_cd/"
            "domains/traffic/signals/signals.json"
        )

    def get_summary(self):

        df = pd.read_csv(
            self.prediction_path
        )

        return {

            "routes":
                df["route_id"].nunique(),

            "high_risk":

                len(

                    df[
                        df[
                            "predicted_risk_level"
                        ] == "High"
                    ]
                ),

            "avg_score":

                round(

                    df[
                        "predicted_congestion_score"
                    ].mean(),

                    2
                )
        }

    def get_predictions(self):

        df = pd.read_csv(
            self.prediction_path
        )

        return df[
            [
                "route_id",
                "checkpoint_name",
                "predicted_risk_level",
                "predicted_congestion_score"
            ]
        ]
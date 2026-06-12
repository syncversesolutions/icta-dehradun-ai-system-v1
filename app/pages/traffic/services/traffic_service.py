import json
import pandas as pd

from pathlib import Path

from config.paths import BASE_DIR


class TrafficService:

    def __init__(self):

        self.state_path = (
            Path(BASE_DIR)
            / "system/state/domains/traffic_state.json"
        )

        self.prediction_path = (
            Path(BASE_DIR)
            / "domains/traffic/data/predictions/traffic_predictions.csv"
        )

        self.signal_path = (
            Path(BASE_DIR)
            / "domains/traffic/signals/signals.json"
        )

        self.graph_path = (
            Path(BASE_DIR)
            / "system/graph/dependency_graph.json"
        )

        self.recommendation_path = (
            Path(BASE_DIR)
            / "system/state/agents/recommendation_agent_state.json"
        )

    # =====================================
    # LOADERS
    # =====================================

    def load_state(self):

        if not self.state_path.exists():

            return {}

        with open(
            self.state_path,
            "r"
        ) as f:

            return json.load(f)

    def load_predictions(self):

        if not self.prediction_path.exists():

            return pd.DataFrame()

        return pd.read_csv(
            self.prediction_path
        )

    def load_signals(self):

        if not self.signal_path.exists():

            return []

        with open(
            self.signal_path,
            "r"
        ) as f:

            return json.load(f)

    def load_dependency_graph(self):

        if not self.graph_path.exists():

            return {}

        with open(
            self.graph_path,
            "r"
        ) as f:

            return json.load(f)

    def load_recommendations(self):

        if not self.recommendation_path.exists():

            return []

        with open(
            self.recommendation_path,
            "r"
        ) as f:

            data = json.load(f)

        return data.get(
            "recommendations",
            []
        )

    # =====================================
    # SUMMARY
    # =====================================

    def get_summary(self):

        state = self.load_state()

        kpis = state.get(
            "kpis",
            {}
        )

        predictions = state.get(
            "predictions",
            {}
        )

        return {

            "status":
                state.get(
                    "status",
                    "unknown"
                ),

            "congestion_score":
                round(
                    kpis.get(
                        "congestion_score",
                        0
                    ) * 100,
                    1
                ),

            "travel_time":
                kpis.get(
                    "travel_time",
                    0
                ),

            "throughput":
                kpis.get(
                    "throughput",
                    0
                ),

            "forecast":
                round(
                    predictions.get(
                        "congestion_next_hour",
                        0
                    ) * 100,
                    1
                )
        }

    # =====================================
    # SIGNALS
    # =====================================

    def get_signals(self):

        return self.load_signals()

    # =====================================
    # PREDICTIONS
    # =====================================

    def get_predictions(self):

        df = self.load_predictions()

        if df.empty:

            return df

        return df[
            [
                "route_id",
                "checkpoint_name",
                "predicted_risk_level",
                "predicted_congestion_score"
            ]
        ]

    # =====================================
    # GRAPH
    # =====================================

    def get_dependency_graph(self):

        return (
            self.load_dependency_graph()
        )

    # =====================================
    # RECOMMENDATIONS
    # =====================================

    def get_recommendations(self):

        recommendations = []

        for rec in self.load_recommendations():

            if rec.get(
                "domain"
            ) == "traffic":

                recommendations.append(
                    rec
                )

        return recommendations
import pandas as pd
import json

from pathlib import Path

from config.paths import BASE_DIR


class AccommodationService:

    def __init__(self):

        self.prediction_path = (
            Path(BASE_DIR)
            / "domains/accommodation/data/predictions/accommodation_predictions.csv"
        )

        self.signal_path = (
            Path(BASE_DIR)
            / "domains/accommodation/signals/signals.json"
        )

        self.state_path = (
            Path(BASE_DIR)
            / "system/state/global/global_state.json"
        )

        self.domain_state_path = (
            Path(BASE_DIR)
            / "system/state/domains/accommodation_state.json"
        )

        self.kpi_path = (
            Path(BASE_DIR)
            / "domains/accommodation/data/kpi/accommodation_kpi.csv"
        )

        self.graph_path = (
            Path(BASE_DIR)
            / "system/graph/dependency_graph.json"
        )

    # =====================================
    # LOADERS
    # =====================================

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

    def load_state(self):

        if not self.state_path.exists():

            return {}

        with open(
            self.state_path,
            "r"
        ) as f:

            return json.load(f)

    def load_domain_state(self):

        if not self.domain_state_path.exists():

            return {}

        with open(
            self.domain_state_path,
            "r"
        ) as f:

            return json.load(f)

    def load_kpis(self):

        if not self.kpi_path.exists():

            return pd.DataFrame()

        return pd.read_csv(
            self.kpi_path
        )

    def load_dependency_graph(self):

        if not self.graph_path.exists():

            return {}

        with open(
            self.graph_path,
            "r"
        ) as f:

            return json.load(f)

    # =====================================
    # SUMMARY
    # =====================================

    def get_summary(self):

        state = (
            self.load_domain_state()
        )

        signals = (
            self.load_signals()
        )

        occupancy = (
            state
            .get("kpis", {})
            .get("occupancy", 0)
        )

        available_beds = (
            state
            .get("kpis", {})
            .get("available_beds", 0)
        )

        forecast = (
            state
            .get("predictions", {})
            .get("occupancy_next_6h", 0)
        )

        return {

            "occupancy":
                round(
                    occupancy * 100,
                    1
                ),

            "available_beds":
                available_beds,

            "forecast":
                round(
                    forecast * 100,
                    1
                ),

            "signals":
                len(signals),

            "state":
                state
        }

    # =====================================
    # CAPACITY SUMMARY
    # =====================================

    def get_capacity_summary(self):

        df = self.load_kpis()

        if df.empty:

            return {}

        return {

            "total_rooms":
                int(
                    df[
                        "total_rooms"
                    ].sum()
                ),

            "occupied_rooms":
                int(
                    df[
                        "occupied_rooms"
                    ].sum()
                ),

            "average_occupancy":
                round(

                    df[
                        "occupancy_rate"
                    ].mean() * 100,

                    1
                ),

            "peak_occupancy":
                round(

                    df[
                        "occupancy_rate"
                    ].max() * 100,

                    1
                )
        }

    # =====================================
    # ACCESSORS
    # =====================================

    def get_prediction_table(self):

        return self.load_predictions()

    def get_signals(self):

        return self.load_signals()

    def get_dependency_graph(self):

        return (
            self.load_dependency_graph()
        )
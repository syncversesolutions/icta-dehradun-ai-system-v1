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

    # =====================================
    # LOAD PREDICTIONS
    # =====================================

    def load_predictions(self):

        if not self.prediction_path.exists():

            return pd.DataFrame()

        return pd.read_csv(
            self.prediction_path
        )

    # =====================================
    # LOAD SIGNALS
    # =====================================

    def load_signals(self):

        if not self.signal_path.exists():

            return []

        with open(
            self.signal_path,
            "r"
        ) as f:

            return json.load(f)

    # =====================================
    # LOAD STATE
    # =====================================

    def load_state(self):

        if not self.state_path.exists():

            return {}

        with open(
            self.state_path,
            "r"
        ) as f:

            return json.load(f)

    # =====================================
    # SUMMARY
    # =====================================

    def get_summary(self):

        df = self.load_predictions()

        signals = self.load_signals()

        state = self.load_state()

        if df.empty:

            return {

                "properties": 0,
                "high_risk": 0,
                "avg_occupancy": 0,
                "signals": 0
            }

        occupancy_column = None

        for col in df.columns:

            if "occupancy" in col.lower():

                occupancy_column = col

                break

        avg_occupancy = 0

        if occupancy_column:

            avg_occupancy = round(

                df[
                    occupancy_column
                ].mean(),

                2
            )

        return {

            "properties":
                len(df),

            "high_risk":
                len(signals),

            "avg_occupancy":
                avg_occupancy,

            "signals":
                len(signals),

            "state":
                state
        }

    # =====================================
    # TABLE
    # =====================================

    def get_prediction_table(self):

        return self.load_predictions()

    # =====================================
    # SIGNALS
    # =====================================

    def get_signals(self):

        return self.load_signals()
import json

from pathlib import Path

from config.paths import BASE_DIR


class CrowdService:

    def __init__(self):

        self.state_path = (

            Path(BASE_DIR)
            / "system/state/global/global_state.json"
        )

        self.signal_path = (

            Path(BASE_DIR)
            / "system/signals/all_signals.json"
        )

        self.impact_path = (

            Path(BASE_DIR)
            / "system/graph/impact_analysis.json"
        )

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
    # LOAD IMPACTS
    # =====================================

    def load_impacts(self):

        if not self.impact_path.exists():

            return []

        with open(
            self.impact_path,
            "r"
        ) as f:

            return json.load(f)

    # =====================================
    # CROWD SUMMARY
    # =====================================

    def get_summary(self):

        state = self.load_state()

        signals = self.load_signals()

        impacts = self.load_impacts()

        crowd_signals = [

            s

            for s in signals

            if s.get(
                "domain"
            ) == "crowd"
        ]

        return {

            "crowd_signals":
                len(crowd_signals),

            "impact_count":
                len(impacts),

            "risk_level":
                state.get(
                    "risk_level",
                    "unknown"
                ),

            "critical_domains":
                len(

                    state.get(
                        "critical_domains",
                        []
                    )
                )
        }

    # =====================================
    # PUBLIC ACCESSORS
    # =====================================

    def get_signals(self):

        return self.load_signals()

    def get_impacts(self):

        return self.load_impacts()

    def get_state(self):

        return self.load_state()
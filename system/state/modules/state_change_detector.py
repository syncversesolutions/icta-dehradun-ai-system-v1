import json

from pathlib import Path
from datetime import datetime

from config.paths import BASE_DIR


class StateChangeDetector:

    def __init__(self):

        self.global_state_path = (
            Path(BASE_DIR)
            / "system/state/global/global_state.json"
        )

    # =====================================
    # LOAD STATE
    # =====================================

    def load_state(self):

        with open(
            self.global_state_path,
            "r"
        ) as f:

            return json.load(f)

    # =====================================
    # SAVE STATE
    # =====================================

    def save_state(
        self,
        state
    ):

        state["updated_at"] = (
            str(datetime.now())
        )

        with open(
            self.global_state_path,
            "w"
        ) as f:

            json.dump(
                state,
                f,
                indent=4
            )

    # =====================================
    # DETECT CHANGES
    # =====================================

    def detect(self):

        state = self.load_state()

        critical_domains = []

        active_signals = []

        risk_level = "low"

        # =================================
        # TRAFFIC
        # =================================

        traffic = state.get(
            "domain_states",
            {}
        ).get(
            "traffic",
            {}
        )

        congestion_score = (
            traffic.get(
                "congestion_score",
                0
            )
        )

        if congestion_score >= 0.80:

            critical_domains.append(
                "traffic"
            )

            active_signals.append(
                "traffic_congestion"
            )

            risk_level = "high"

        # =================================
        # CROWD
        # =================================

        crowd = state.get(
            "domain_states",
            {}
        ).get(
            "crowd",
            {}
        )

        density_score = crowd.get(
            "density_score",
            0
        )

        if density_score >= 0.80:

            critical_domains.append(
                "crowd"
            )

            active_signals.append(
                "crowd_overload"
            )

            risk_level = "high"

        # =================================
        # ACCOMMODATION
        # =================================

        accommodation = state.get(
            "domain_states",
            {}
        ).get(
            "accommodation",
            {}
        )

        occupancy_score = (
            accommodation.get(
                "occupancy_score",
                0
            )
        )

        if occupancy_score >= 0.90:

            critical_domains.append(
                "accommodation"
            )

            active_signals.append(
                "accommodation_full"
            )

            risk_level = "high"

        # =================================
        # HEALTH
        # =================================

        health = state.get(
            "domain_states",
            {}
        ).get(
            "health",
            {}
        )

        incident_score = health.get(
            "incident_score",
            0
        )

        if incident_score >= 0.80:

            critical_domains.append(
                "health"
            )

            active_signals.append(
                "medical_alert"
            )

            risk_level = "critical"

        # =================================
        # UPDATE STATE
        # =================================

        state["critical_domains"] = (
            sorted(
                list(
                    set(
                        critical_domains
                    )
                )
            )
        )

        state["active_signals"] = (
            sorted(
                list(
                    set(
                        active_signals
                    )
                )
            )
        )

        state["risk_level"] = (
            risk_level
        )

        self.save_state(
            state
        )

        return state

    # =====================================
    # DISPLAY
    # =====================================

    def display(self):

        state = self.detect()

        print("\n")
        print("=" * 60)
        print("STATE CHANGE DETECTOR")
        print("=" * 60)

        print(
            "\nRisk Level:"
        )

        print(
            state["risk_level"]
        )

        print(
            "\nCritical Domains:"
        )

        for domain in state[
            "critical_domains"
        ]:

            print(
                f"• {domain}"
            )

        print(
            "\nActive Signals:"
        )

        for signal in state[
            "active_signals"
        ]:

            print(
                f"• {signal}"
            )

        print("\n")
        print("=" * 60)
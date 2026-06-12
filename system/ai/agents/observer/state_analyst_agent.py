import json

from pathlib import Path
from datetime import datetime

from config.paths import BASE_DIR


class StateAnalystAgent:

    def __init__(self):

        self.global_state_path = (
            Path(BASE_DIR)
            / "system/state/global/global_state.json"
        )

        self.agent_state_path = (
            Path(BASE_DIR)
            / "system/state/agents/state_analyst_state.json"
        )

    # =====================================
    # LOAD GLOBAL STATE
    # =====================================

    def load_global_state(self):

        if not self.global_state_path.exists():

            return {}

        with open(
            self.global_state_path,
            "r"
        ) as f:

            return json.load(f)

    # =====================================
    # ANALYZE STATE
    # =====================================

    def analyze(self):

        state = self.load_global_state()

        observations = []

        risk_level = state.get(
            "risk_level",
            "low"
        )

        system_status = state.get(
            "system_status",
            "active"
        )

        active_alerts = state.get(
            "active_alerts",
            []
        )

        critical_domains = state.get(
            "critical_domains",
            []
        )

        if risk_level == "high":

            observations.append(
                "High system risk detected"
            )

        if risk_level == "critical":

            observations.append(
                "Critical system condition"
            )

        if len(active_alerts) > 0:

            observations.append(
                f"{len(active_alerts)} active alerts present"
            )

        if system_status != "active":

            observations.append(
                f"System status is {system_status}"
            )

        if len(observations) == 0:

            observations.append(
                "System operating normally"
            )

        result = {

            "agent":
                "state_analyst_agent",

            "status":
                "completed",

            "timestamp":
                str(datetime.now()),

            "risk_level":
                risk_level,

            "system_status":
                system_status,

            "critical_domains":
                critical_domains,

            "active_alert_count":
                len(active_alerts),

            "observation_count":
                len(observations),

            "observations":
                observations
        }

        self.save_agent_state(
            result
        )

        return result

    # =====================================
    # SAVE STATE
    # =====================================

    def save_agent_state(
        self,
        state
    ):

        self.agent_state_path.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        with open(
            self.agent_state_path,
            "w"
        ) as f:

            json.dump(
                state,
                f,
                indent=4
            )

    # =====================================
    # DISPLAY
    # =====================================

    def display(self):

        result = self.analyze()

        print("\n")
        print("=" * 60)
        print("STATE ANALYST AGENT")
        print("=" * 60)

        print(
            f"\nRisk Level: "
            f"{result['risk_level']}"
        )

        print(
            f"\nCritical Domains: "
            f"{result['critical_domains']}"
        )

        print("\nObservations:")

        for item in result[
            "observations"
        ]:

            print(
                f"• {item}"
            )

        print("=" * 60)
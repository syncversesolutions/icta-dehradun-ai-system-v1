from datetime import datetime


class SimulationEngine:

    def __init__(self):

        self.scenarios = []

    # ========================================
    # TRAFFIC CASCADE SIMULATION
    # ========================================

    def simulate_traffic_cascade(self):

        scenario = {

            "scenario":
                "traffic_cascade",

            "trigger":
                "occupancy surge",

            "predicted_effect":

                "checkpoint congestion increase",

            "response":

                "activate rerouting",

            "timestamp":
                str(datetime.now())
        }

        self.scenarios.append(
            scenario
        )

    # ========================================
    # CROWD CASCADE SIMULATION
    # ========================================

    def simulate_crowd_cascade(self):

        scenario = {

            "scenario":
                "crowd_pressure",

            "trigger":
                "high accommodation inflow",

            "predicted_effect":

                "queue buildup",

            "response":

                "enable redistribution",

            "timestamp":
                str(datetime.now())
        }

        self.scenarios.append(
            scenario
        )

    # ========================================
    # HEALTH CASCADE SIMULATION
    # ========================================

    def simulate_health_cascade(self):

        scenario = {

            "scenario":
                "health_pressure",

            "trigger":
                "high crowd density",

            "predicted_effect":

                "medical response overload",

            "response":

                "increase medical deployment",

            "timestamp":
                str(datetime.now())
        }

        self.scenarios.append(
            scenario
        )

    # ========================================
    # RUN SIMULATION
    # ========================================

    def run(self):

        self.simulate_traffic_cascade()

        self.simulate_crowd_cascade()

        self.simulate_health_cascade()

        # =====================================
        # SAVE SCENARIOS
        # =====================================

        import json

        from pathlib import Path

        from config.paths import BASE_DIR

        scenario_path = (

            Path(BASE_DIR)

            / "system/prediction/scenarios/latest_scenarios.json"
        )

        scenario_path.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        with open(
            scenario_path,
            "w"
        ) as f:

            json.dump(
                {

                    "generated_at":
                        str(datetime.now()),

                    "scenario_count":
                        len(
                            self.scenarios
                        ),

                    "scenarios":
                        self.scenarios
                },
                f,
                indent=4
            )

        print(
            "\nScenario simulation complete ✅"
        )

        return self.scenarios
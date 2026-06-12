import json

from pathlib import Path
from datetime import datetime

from config.paths import BASE_DIR


class StateAggregator:

    def __init__(self):

        self.global_state_path = (

            Path(BASE_DIR)
            / "system/state/global/global_state.json"
        )

        self.memory_path = (

            Path(BASE_DIR)
            / "system/memory/history/episodic_memory.json"
        )

        self.forecast_path = (

            Path(BASE_DIR)
            / "system/prediction/forecasts/latest_forecast.json"
        )

        self.scenario_path = (

            Path(BASE_DIR)
            / "system/prediction/scenarios/latest_scenarios.json"
        )

        self.autonomy_path = (

            Path(BASE_DIR)
            / "system/autonomy/state/autonomy_state.json"
        )

    # =====================================
    # LOAD JSON
    # =====================================

    def load_json(
        self,
        path,
        default=None
    ):

        if default is None:

            default = {}

        if not path.exists():

            return default

        with open(
            path,
            "r"
        ) as f:

            return json.load(f)

    # =====================================
    # SAVE GLOBAL STATE
    # =====================================

    def save_global_state(
        self,
        state
    ):

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
    # AGGREGATE
    # =====================================

    def aggregate(self):

        state = self.load_json(
            self.global_state_path,
            {}
        )

        memory = self.load_json(
            self.memory_path,
            []
        )

        forecasts = self.load_json(
            self.forecast_path,
            {}
        )

        scenarios = self.load_json(
            self.scenario_path,
            {}
        )

        autonomy = self.load_json(
            self.autonomy_path,
            {}
        )

        # =====================================
        # COUNTS
        # =====================================

        state[
            "memory_episode_count"
        ] = len(memory)

        state[
            "forecast_count"
        ] = len(
            forecasts.get(
                "forecasts",
                []
            )
        )

        state[
            "scenario_count"
        ] = len(
            scenarios.get(
                "scenarios",
                []
            )
        )

        state[
            "autonomous_action_count"
        ] = autonomy.get(
            "actions_executed",
            0
        )

        state[
            "recovery_count"
        ] = autonomy.get(
            "recoveries",
            0
        )

        # =====================================
        # EXECUTION TIMESTAMPS
        # =====================================

        state[
            "last_forecast_execution"
        ] = forecasts.get(
            "generated_at"
        )

        state[
            "last_simulation_execution"
        ] = scenarios.get(
            "generated_at"
        )

        state[
            "last_autonomous_execution"
        ] = autonomy.get(
            "last_execution"
        )

        # =====================================
        # UPDATE TIMESTAMP
        # =====================================

        state[
            "updated_at"
        ] = str(
            datetime.now()
        )

        self.save_global_state(
            state
        )

        print(
            "\nGlobal state aggregated ✅"
        )

        return state
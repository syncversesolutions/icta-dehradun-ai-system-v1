import json

from pathlib import Path
from datetime import datetime

from config.paths import BASE_DIR


class WorkflowEngine:

    def __init__(self):

        self.active_workflows_path = (

            Path(BASE_DIR)

            / "system/state/workflows"

            / "active_workflows.json"
        )

        self.history_path = (

            Path(BASE_DIR)

            / "system/state/workflows"

            / "workflow_history.json"
        )

        self.global_state_path = (

            Path(BASE_DIR)

            / "system/state/global"

            / "global_state.json"
        )

    # ====================================
    # LOAD JSON
    # ====================================

    def load_json(self, path):

        if not path.exists():

            return {}

        with open(path, "r") as f:

            return json.load(f)

    # ====================================
    # SAVE JSON
    # ====================================

    def save_json(
        self,
        path,
        data
    ):

        path.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        with open(path, "w") as f:

            json.dump(
                data,
                f,
                indent=4
            )

    # ====================================
    # EXECUTE SINGLE WORKFLOW
    # ====================================

    def execute_workflow(
        self,
        workflow
    ):

        workflow["status"] = (
            "completed"
        )

        workflow["executed_at"] = (
            str(datetime.now())
        )

        return workflow

    # ====================================
    # UPDATE GLOBAL STATE
    # ====================================

    def update_global_state(
        self,
        completed_workflows
    ):

        state = self.load_json(
            self.global_state_path
        )

        state[
            "active_workflows"
        ] = []

        state[
            "last_workflow_execution"
        ] = str(
            datetime.now()
        )

        state[
            "event_history_count"
        ] = (

            state.get(
                "event_history_count",
                0
            )

            + len(
                completed_workflows
            )
        )

        self.save_json(
            self.global_state_path,
            state
        )

    # ====================================
    # EXECUTE
    # ====================================

    def execute(self):

        active = self.load_json(
            self.active_workflows_path
        )

        workflows = active.get(
            "active_workflows",
            []
        )

        completed = []

        for workflow in workflows:

            result = (
                self.execute_workflow(
                    workflow
                )
            )

            completed.append(
                result
            )

        # --------------------------
        # Update Active Workflows
        # --------------------------

        active[
            "active_workflows"
        ] = completed

        active[
            "last_execution"
        ] = str(
            datetime.now()
        )

        self.save_json(
            self.active_workflows_path,
            active
        )

        # --------------------------
        # History
        # --------------------------

        history = self.load_json(
            self.history_path
        )

        if (
            "workflow_runs"
            not in history
        ):

            history[
                "workflow_runs"
            ] = []

        history[
            "workflow_runs"
        ].extend(
            completed
        )

        self.save_json(
            self.history_path,
            history
        )

        # --------------------------
        # Global State
        # --------------------------

        self.update_global_state(
            completed
        )

        print("\n")
        print("=" * 60)
        print(
            "WORKFLOW ENGINE"
        )
        print("=" * 60)

        print(

            f"\nExecuted "

            f"{len(completed)} "

            f"workflows"
        )

        print("\n")
        print("=" * 60)

        return completed
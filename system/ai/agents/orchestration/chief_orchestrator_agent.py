import json

from pathlib import Path
from datetime import datetime

from config.paths import BASE_DIR


class ChiefOrchestratorAgent:

    def __init__(self):

        self.recommendation_path = (

            Path(BASE_DIR)

            / "system/state/agents"

            / "recommendation_agent_state.json"
        )

        self.workflow_path = (

            Path(BASE_DIR)

            / "system/state/workflows"

            / "active_workflows.json"
        )

    # =====================================
    # LOAD JSON
    # =====================================

    def load_json(self, path):

        if not path.exists():

            return {}

        with open(path, "r") as f:

            return json.load(f)

    # =====================================
    # SAVE WORKFLOWS
    # =====================================

    def save_workflows(
        self,
        workflow_data
    ):

        self.workflow_path.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        with open(
            self.workflow_path,
            "w"
        ) as f:

            json.dump(
                workflow_data,
                f,
                indent=4
            )

    # =====================================
    # WORKFLOW MAPPING
    # =====================================

    def get_workflow_name(
        self,
        action
    ):

        workflow_map = {

            "Activate alternate route":

                "Traffic_Rerouting_Workflow",

            "Redistribute crowd flow":

                "Crowd_Redistribution_Workflow",

            "Prepare medical response team":

                "Medical_Response_Workflow",

            "Raise operational alert":

                "Operational_Alert_Workflow",

            "Notify emergency coordination":

                "Emergency_Coordination_Workflow"
        }

        return workflow_map.get(

            action,

            "Generic_Response_Workflow"
        )

    # =====================================
    # CREATE WORKFLOWS
    # =====================================

    def create_workflows(self):

        recommendations = self.load_json(
            self.recommendation_path
        )

        recommendation_list = (

            recommendations.get(
                "recommendations",
                []
            )
        )

        workflows = []

        counter = 1

        for item in recommendation_list:

            workflow = {

                "workflow_id":

                    f"WF-{counter:03d}",

                "workflow_name":

                    self.get_workflow_name(
                        item["action"]
                    ),

                "domain":

                    item["domain"],

                "priority":

                    item.get(
                        "priority",
                        "medium"
                    ),

                "status":

                    "pending",

                "created_at":

                    str(
                        datetime.now()
                    )
            }

            workflows.append(
                workflow
            )

            counter += 1

        result = {

            "generated_at":

                str(
                    datetime.now()
                ),

            "workflow_count":

                len(workflows),

            "active_workflows":

                workflows
        }

        self.save_workflows(
            result
        )

        return {

            "agent":

                "chief_orchestrator_agent",

            "status":

                "completed",

            "workflow_count":

                len(workflows)
        }

    # =====================================
    # DISPLAY
    # =====================================

    def display(self):

        result = (
            self.create_workflows()
        )

        print("\n")
        print("=" * 60)
        print(
            "CHIEF ORCHESTRATOR"
        )
        print("=" * 60)

        print(

            f"\nWorkflows Created: "

            f"{result['workflow_count']}"
        )

        print("\n")
        print("=" * 60)
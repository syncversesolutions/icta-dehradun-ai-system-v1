import json

from pathlib import Path
from datetime import datetime

from config.paths import BASE_DIR


class RecommendationAgent:

    def __init__(self):

        self.dependency_state_path = (

            Path(BASE_DIR)

            / "system/state/agents"

            / "dependency_agent_state.json"
        )

        self.agent_state_path = (

            Path(BASE_DIR)

            / "system/state/agents"

            / "recommendation_agent_state.json"
        )

    # =====================================
    # LOAD JSON
    # =====================================

    def load_json(self, path):

        if not path.exists():

            return {}

        with open(
            path,
            "r"
        ) as f:

            return json.load(f)

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
    # DOMAIN ACTION MAP
    # =====================================

    def get_domain_actions(self):

        return {

            "traffic":

                "Activate alternate route strategy",

            "crowd":

                "Redistribute pilgrim flow",

            "health":

                "Increase ambulance readiness",

            "tourism":

                "Issue route advisory update",

            "governance":

                "Notify emergency coordination team",

            "system":

                "Raise operational alert level",

            "accommodation":

                "Prepare overflow accommodation"
        }

    # =====================================
    # GENERATE
    # =====================================

    def generate(self):

        dependency_state = (

            self.load_json(
                self.dependency_state_path
            )
        )

        affected_domains = (

            dependency_state.get(
                "affected_domains",
                []
            )
        )

        action_map = (
            self.get_domain_actions()
        )

        recommendations = []

        for domain in affected_domains:

            if domain in action_map:

                recommendations.append({

                    "domain":
                        domain,

                    "priority":
                        "high",

                    "action":
                        action_map[domain]
                })

        result = {

            "agent":
                "recommendation_agent",

            "status":
                "completed",

            "timestamp":
                str(
                    datetime.now()
                ),

            "recommendation_count":
                len(
                    recommendations
                ),

            "recommendations":
                recommendations
        }

        self.save_agent_state(
            result
        )

        return result

    # =====================================
    # DISPLAY
    # =====================================

    def display(self):

        result = self.generate()

        print("\n")
        print("=" * 60)
        print(
            "RECOMMENDATION AGENT"
        )
        print("=" * 60)

        for item in result[
            "recommendations"
        ]:

            print(

                f"• "

                f"{item['domain']}"

                f" → "

                f"{item['action']}"
            )

        print("\n")
        print("=" * 60)
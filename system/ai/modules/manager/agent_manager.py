import json

from pathlib import Path
from datetime import datetime

from config.paths import BASE_DIR

# ==========================================
# AGENT IMPORTS
# ==========================================

from system.ai.agents.observer.state_analyst_agent import (
    StateAnalystAgent
)

from system.ai.agents.reasoning.dependency_agent import (
    DependencyAgent
)

from system.ai.agents.optimization.recommendation_agent import (
    RecommendationAgent
)

from system.ai.agents.orchestration.chief_orchestrator_agent import (
    ChiefOrchestratorAgent
)


class AgentManager:

    def __init__(self):

        self.registry_path = (

            Path(BASE_DIR)

            / "architecture"

            / "AGENT_REGISTRY.json"
        )

        self.history_path = (

            Path(BASE_DIR)

            / "runtime"

            / "agent_runs"

            / "agent_execution_history.json"
        )

        self.registry = (
            self.load_registry()
        )

    # =====================================
    # LOAD REGISTRY
    # =====================================

    def load_registry(self):

        if not self.registry_path.exists():

            return {}

        with open(
            self.registry_path,
            "r"
        ) as f:

            return json.load(f)

    # =====================================
    # DISPLAY REGISTRY
    # =====================================

    def display_registry(self):

        print("\n")
        print("=" * 60)
        print("AGENT REGISTRY")
        print("=" * 60)

        sorted_agents = sorted(

            self.registry.items(),

            key=lambda x:
            x[1].get(
                "priority",
                999
            )
        )

        for name, config in sorted_agents:

            print(

                f"{name} | "

                f"Enabled: "
                f"{config.get('enabled')} | "

                f"Priority: "
                f"{config.get('priority')}"
            )

        print("=" * 60)

    # =====================================
    # CREATE AGENT
    # =====================================

    def create_agent(

        self,
        agent_name

    ):

        agent_map = {

            "state_analyst_agent":
                StateAnalystAgent,

            "dependency_agent":
                DependencyAgent,

            "recommendation_agent":
                RecommendationAgent,

            "chief_orchestrator_agent":
                ChiefOrchestratorAgent
        }

        agent_class = agent_map.get(
            agent_name
        )

        if agent_class:

            return agent_class()

        return None

    # =====================================
    # EXECUTE AGENT
    # =====================================

    def execute_agent(

        self,
        agent

    ):

        if hasattr(
            agent,
            "analyze"
        ):

            return (
                agent.analyze()
            )

        if hasattr(
            agent,
            "generate"
        ):

            return (
                agent.generate()
            )

        if hasattr(
            agent,
            "create_workflows"
        ):

            return (
                agent.create_workflows()
            )

        raise Exception(
            "No executable method found"
        )

    # =====================================
    # SAVE HISTORY
    # =====================================

    def save_history(

        self,
        execution_log

    ):

        self.history_path.parent.mkdir(

            parents=True,
            exist_ok=True
        )

        history = {

            "executed_at":
                str(
                    datetime.now()
                ),

            "executed_agents":
                execution_log
        }

        with open(
            self.history_path,
            "w"
        ) as f:

            json.dump(

                history,
                f,
                indent=4
            )

    # =====================================
    # RUN AGENTS
    # =====================================

    def run_agents(self):

        print("\n")
        print("=" * 60)
        print("AGENT MANAGER")
        print("=" * 60)

        execution_log = []

        sorted_agents = sorted(

            self.registry.items(),

            key=lambda x:
            x[1].get(
                "priority",
                999
            )
        )

        for agent_name, config in sorted_agents:

            if not config.get(
                "enabled",
                False
            ):

                continue

            print(
                f"\nRunning: "
                f"{agent_name}"
            )

            try:

                agent = (
                    self.create_agent(
                        agent_name
                    )
                )

                if agent is None:

                    raise Exception(
                        "Agent not found"
                    )

                result = (
                    self.execute_agent(
                        agent
                    )
                )

                execution_log.append({

                    "agent":
                        agent_name,

                    "status":
                        result.get(
                            "status",
                            "completed"
                        ),

                    "timestamp":
                        str(
                            datetime.now()
                        )
                })

            except Exception as e:

                print(
                    f"Failed: "
                    f"{agent_name}"
                )

                print(str(e))

                execution_log.append({

                    "agent":
                        agent_name,

                    "status":
                        "failed",

                    "error":
                        str(e),

                    "timestamp":
                        str(
                            datetime.now()
                        )
                })

        self.save_history(
            execution_log
        )

        print("\n")
        print(
            "Execution Complete"
        )

        print(
            str(
                datetime.now()
            )
        )

        print("=" * 60)

        return execution_log
from datetime import datetime

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


class AgentRuntime:

    def __init__(self):

        self.state_agent = (
            StateAnalystAgent()
        )

        self.dependency_agent = (
            DependencyAgent()
        )

        self.recommendation_agent = (
            RecommendationAgent()
        )

        self.orchestrator_agent = (
            ChiefOrchestratorAgent()
        )

    # ===================================
    # RUN ALL AGENTS
    # ===================================

    def run(self):

        print("\n")
        print("=" * 60)
        print("AGENT RUNTIME")
        print("=" * 60)

        self.state_agent.analyze()

        self.dependency_agent.analyze()

        self.recommendation_agent.generate()

        self.orchestrator_agent.create_workflows()

        print(
            "\nExecution Complete"
        )

        print(
            datetime.now()
        )

        print("=" * 60)
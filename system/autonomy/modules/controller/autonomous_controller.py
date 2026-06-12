from system.autonomy.modules.workflow.workflow_engine import (
    WorkflowEngine
)

from system.autonomy.modules.executor.adaptive_executor import (
    AdaptiveExecutor
)

from system.autonomy.modules.healing.self_healing_engine import (
    SelfHealingEngine
)


class AutonomousController:

    def __init__(self):

        self.workflow_engine = (
            WorkflowEngine()
        )

        self.executor = (
            AdaptiveExecutor()
        )

        self.healing_engine = (
            SelfHealingEngine()
        )

    # ========================================
    # BUILD EXECUTION PLAN
    # ========================================

    def build_execution_plan(
        self,
        scenarios
    ):

        actions = []

        for scenario in scenarios:

            response = scenario.get(
                "response"
            )

            if response:

                actions.append(
                    response
                )

        return {

            "actions":
                actions
        }

    # ========================================
    # RUN AUTONOMOUS FLOW
    # ========================================

    def run(
        self,
        execution_plan
    ):

        workflow = (

            self.workflow_engine
            .create_workflow(

                workflow_name=
                    "adaptive_response",

                actions=
                    execution_plan[
                        "actions"
                    ]
            )
        )

        executed = (

            self.workflow_engine
            .execute_workflow(
                workflow
            )
        )

        logs = (

            self.executor.execute(
                executed
            )
        )

        recoveries = (

            self.healing_engine
            .auto_heal(
                logs
            )
        )
        
        # =====================================
        # SAVE AUTONOMY STATE
        # =====================================

        import json

        from pathlib import Path

        from datetime import datetime

        from config.paths import BASE_DIR

        autonomy_state_path = (

            Path(BASE_DIR)

            / "system/autonomy/state/autonomy_state.json"
        )

        autonomy_state_path.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        with open(
            autonomy_state_path,
            "w"
        ) as f:

            json.dump(
                {

                    "last_execution":
                        str(datetime.now()),

                    "actions_executed":
                        len(logs),

                    "recoveries":
                        len(recoveries)
                },
                f,
                indent=4
            )


        return {

            "workflow":
                executed,

            "execution_logs":
                logs,

            "recoveries":
                recoveries
        }

    # ========================================
    # RUN FROM SCENARIOS
    # ========================================

    def run_from_scenarios(
        self,
        scenarios
    ):

        execution_plan = (

            self.build_execution_plan(
                scenarios
            )
        )

        return self.run(
            execution_plan
        )
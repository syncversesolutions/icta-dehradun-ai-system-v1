from services.state_service import (
    StateService
)
class OrchestrationService:
    def __init__(self):
        self.state_service = (
            StateService()
        )
    # ========================================
    # GET WORKFLOWS
    # ========================================
    def get_workflows(self):
        state = (
            self.state_service
            .get_state()
        )
        workflows = []
        for workflow in state.get(
            "active_workflows",
            []
        ):
            workflows.append({
                "workflow":
                    workflow,
                "status":
                    "running"
            })
        return workflows
    # ========================================
    # GET ACTIONS
    # ========================================
    def get_actions(self):
        state = (
            self.state_service
            .get_state()
        )
        actions = []
        for alert in state.get(
            "active_alerts",
            []
        ):
            actions.append(
                f"Responding to "
                f"{alert.get('source_signal', 'unknown')}"
            )
        return actions
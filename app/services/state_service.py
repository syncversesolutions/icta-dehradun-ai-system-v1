import json
from pathlib import Path
from config.paths import BASE_DIR
class StateService:
    def __init__(self):
        self.state_path = (
            Path(BASE_DIR) /
            "system/state/system_state.json"
        )
    # ========================================
    # GET STATE
    # ========================================
    def get_state(self):
        with open(
            self.state_path,
            "r"
        ) as f:
            state = json.load(f)
        # ====================================
        # SAFE DEFAULTS
        # ====================================
        defaults = {
            "system_status":
                "active",
            "risk_level":
                "low",
            "active_alerts":
                [],
            "critical_domains":
                [],
            "active_workflows":
                [],
            "last_pipeline_run":
                None,
            "domains_active":
                [],
            "artifacts_generated":
                []
        }
        for key, value in defaults.items():
            if key not in state:
                state[key] = value
        return state
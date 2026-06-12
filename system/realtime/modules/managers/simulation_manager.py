import json
from copy import deepcopy
from pathlib import Path
from config.paths import BASE_DIR
class SimulationManager:
    def __init__(self):
        # ====================================
        # PROJECT ROOT
        # ====================================
        self.base_dir = (
            Path(BASE_DIR)
        )
        # ====================================
        # RUNTIME ROOT
        # ====================================
        self.runtime_root = (
            self.base_dir /
            "runtime"
        )
        # ====================================
        # SNAPSHOT ROOT
        # ====================================
        self.snapshot_root = (
            self.runtime_root /
            "snapshots"
        )
        # ====================================
        # SIMULATION ROOT
        # ====================================
        self.simulation_root = (
            self.runtime_root /
            "simulations"
        )
    # ========================================
    # LOAD SNAPSHOT
    # ========================================
    def load_snapshot(
        self,
        snapshot_name
    ):
        snapshot_path = (
            self.snapshot_root /
            snapshot_name /
            "system_state.json"
        )
        if not snapshot_path.exists():
            print(
                "\nSnapshot not found"
            )
            return None
        with open(
            snapshot_path,
            "r"
        ) as f:
            snapshot = json.load(f)
        return snapshot
    # ========================================
    # RUN SIMULATION
    # ========================================
    def run_simulation(
        self,
        snapshot_name,
        occupancy_delta=0
    ):
        # ====================================
        # LOAD BASELINE
        # ====================================
        baseline = self.load_snapshot(
            snapshot_name
        )
        if baseline is None:
            return None
        # ====================================
        # COPY BASELINE
        # ====================================
        projected_state = deepcopy(
            baseline
        )
        # ====================================
        # CURRENT CONDITIONS
        # ====================================
        current_risk = projected_state.get(
            "risk_level",
            "low"
        )
        domains = projected_state.get(
            "domains_active",
            []
        )
        # ====================================
        # TRAFFIC IMPACT
        # ====================================
        traffic_impact = (
            occupancy_delta * 1.8
        )
        # ====================================
        # CROWD IMPACT
        # ====================================
        crowd_impact = (
            occupancy_delta * 1.4
        )
        # ====================================
        # MEDICAL IMPACT
        # ====================================
        medical_impact = (
            occupancy_delta * 0.8
        )
        # ====================================
        # PROJECTED RISK
        # ====================================
        projected_risk = "low"
        if occupancy_delta >= 20:
            projected_risk = "medium"
        if occupancy_delta >= 40:
            projected_risk = "high"
        if occupancy_delta >= 60:
            projected_risk = "critical"
        # ====================================
        # PROJECTED ALERTS
        # ====================================
        projected_alerts = []
        if traffic_impact > 40:
            projected_alerts.append({
                "type":
                    "Projected Traffic Alert",
                "severity":
                    "HIGH"
            })
        if crowd_impact > 50:
            projected_alerts.append({
                "type":
                    "Projected Crowd Alert",
                "severity":
                    "CRITICAL"
            })
        # ====================================
        # PROJECTED WORKFLOWS
        # ====================================
        projected_workflows = [
            "adaptive_response",
            "traffic_diversion",
            "crowd_stabilization"
        ]
        # ====================================
        # PROJECTED DOMAINS
        # ====================================
        projected_domains = list(
            set(
                domains + [
                    "traffic",
                    "crowd",
                    "medical"
                ]
            )
        )
        # ====================================
        # BUILD RESULT
        # ====================================
        simulation_result = {
            "snapshot":
                snapshot_name,
            "occupancy_delta":
                occupancy_delta,
            "baseline_risk":
                current_risk,
            "projected_risk":
                projected_risk,
            "traffic_impact":
                traffic_impact,
            "crowd_impact":
                crowd_impact,
            "medical_impact":
                medical_impact,
            "projected_alerts":
                projected_alerts,
            "projected_workflows":
                projected_workflows,
            "affected_domains":
                projected_domains
        }
        return simulation_result
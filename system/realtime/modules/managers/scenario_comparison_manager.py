class ScenarioComparisonManager:
    def __init__(self):
        pass
    # ========================================
    # COMPARE SCENARIOS
    # ========================================
    def compare(
        self,
        simulations
    ):
        comparison = []
        risk_scores = {
            "low": 1,
            "medium": 2,
            "high": 3,
            "critical": 4
        }
        for simulation in simulations:
            projected_risk = simulation.get(
                "projected_risk",
                "low"
            )
            alerts = simulation.get(
                "projected_alerts",
                []
            )
            workflows = simulation.get(
                "projected_workflows",
                []
            )
            domains = simulation.get(
                "affected_domains",
                []
            )
            comparison.append({
                "snapshot":
                    simulation.get(
                        "snapshot"
                    ),
                "occupancy_delta":
                    simulation.get(
                        "occupancy_delta"
                    ),
                "risk":
                    projected_risk,
                "risk_score":
                    risk_scores.get(
                        projected_risk,
                        1
                    ),
                "alert_count":
                    len(alerts),
                "workflow_count":
                    len(workflows),
                "affected_domains":
                    len(domains)
            })
        # ====================================
        # SORT BY RISK
        # ====================================
        comparison = sorted(
            comparison,
            key=lambda x:
                x["risk_score"],
            reverse=True
        )
        return comparison
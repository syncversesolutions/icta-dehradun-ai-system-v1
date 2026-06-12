# ============================================
# IMPORTS
# ============================================

import json
from pathlib import Path


# ============================================
# SERVICE
# ============================================

class IntelligenceCenterService:

    def __init__(self):

        self.project_root = (
            Path(__file__)
            .resolve()
            .parents[4]
        )

        self.global_state_path = (
            self.project_root
            / "system"
            / "state"
            / "global"
            / "global_state.json"
        )

        self.state_analyst_path = (
            self.project_root
            / "system"
            / "state"
            / "agents"
            / "state_analyst_state.json"
        )

        self.impact_analysis_path = (
            self.project_root
            / "system"
            / "graph"
            / "impact_analysis.json"
        )

        self.forecast_path = (
            self.project_root
            / "system"
            / "prediction"
            / "forecasts"
            / "latest_forecast.json"
        )

        self.scenario_path = (
            self.project_root
            / "system"
            / "prediction"
            / "scenarios"
            / "latest_scenarios.json"
        )

        self.recommendation_path = (
            self.project_root
            / "system"
            / "state"
            / "agents"
            / "recommendation_agent_state.json"
        )

    # ============================================
    # JSON LOADER
    # ============================================

    def _load_json(self, file_path):

        try:

            with open(
                file_path,
                "r"
            ) as file:

                return json.load(file)

        except Exception:

            return {}

    # ============================================
    # EXECUTIVE ASSESSMENT
    # ============================================

    def get_executive_assessment(self):

        return self._load_json(
            self.state_analyst_path
        )

    # ============================================
    # ACTIVE SIGNALS
    # ============================================

    def get_active_signals(self):

        state = self._load_json(
            self.global_state_path
        )

        return state.get(
            "active_signals",
            []
        )

    # ============================================
    # IMPACT ANALYSIS
    # ============================================

    def get_impact_analysis(self):

        return self._load_json(
            self.impact_analysis_path
        )

    # ============================================
    # IMPACT SUMMARY
    # ============================================

    def get_impact_summary(self):

        impacts = self.get_impact_analysis()

        affected_domains = set()

        checkpoints = set()

        for item in impacts:

            signal = item.get(
                "signal",
                {}
            )

            checkpoint = signal.get(
                "checkpoint_name"
            )

            if checkpoint:

                checkpoints.add(
                    checkpoint
                )

            downstream_impacts = item.get(
                "downstream_impacts",
                []
            )

            for impact in downstream_impacts:

                try:

                    domain = (
                        impact.split(".")[0]
                    )

                    affected_domains.add(
                        domain
                    )

                except Exception:

                    pass

        return {

            "impact_count":
                len(impacts),

            "affected_domain_count":
                len(
                    affected_domains
                ),

            "affected_domains":
                sorted(
                    list(
                        affected_domains
                    )
                ),

            "high_risk_checkpoint_count":
                len(
                    checkpoints
                ),

            "high_risk_checkpoints":
                sorted(
                    list(
                        checkpoints
                    )
                )
        }

    # ============================================
    # FORECASTS
    # ============================================

    def get_forecasts(self):

        forecast_data = self._load_json(
            self.forecast_path
        )

        return forecast_data.get(
            "forecasts",
            []
        )

    # ============================================
    # SCENARIOS
    # ============================================

    def get_scenarios(self):

        scenario_data = self._load_json(
            self.scenario_path
        )

        return scenario_data.get(
            "scenarios",
            []
        )

    # ============================================
    # RECOMMENDATIONS
    # ============================================

    def get_recommendations(self):

        recommendation_data = self._load_json(
            self.recommendation_path
        )

        return recommendation_data.get(
            "recommendations",
            []
        )

    # ============================================
    # MASTER SNAPSHOT
    # ============================================

    def get_intelligence_snapshot(self):

        executive = (
            self.get_executive_assessment()
        )

        return {

            "system_status":
                executive.get(
                    "system_status",
                    "unknown"
                ),

            "risk_level":
                executive.get(
                    "risk_level",
                    "unknown"
                ),

            "critical_domains":
                executive.get(
                    "critical_domains",
                    []
                ),

            "observations":
                executive.get(
                    "observations",
                    []
                ),

            "signals":
                self.get_active_signals(),

            "impacts":
                self.get_impact_analysis(),

            "impact_summary":
                self.get_impact_summary(),

            "forecasts":
                self.get_forecasts(),

            "scenarios":
                self.get_scenarios(),

            "recommendations":
                self.get_recommendations()
        }



    # ============================================
    # KPI SUMMARY
    # ============================================

    def get_kpis(self):

        snapshot = (
            self.get_intelligence_snapshot()
        )

        return {

            "risk_level":
                snapshot.get(
                    "risk_level",
                    "UNKNOWN"
                ).upper(),

            "active_signals":
                len(
                    snapshot.get(
                        "signals",
                        []
                    )
                ),

            "forecast_count":
                len(
                    snapshot.get(
                        "forecasts",
                        []
                    )
                ),

            "autonomous_actions":
                len(
                    snapshot.get(
                        "recommendations",
                        []
                    )
                )
        }

    # ============================================
    # DEPENDENCY GRAPH
    # ============================================

    def get_dependency_graph(self):

        graph_path = (
            self.project_root
            / "system"
            / "graph"
            / "dependency_graph.json"
        )

        return self._load_json(
            graph_path
        )
# ============================================
# IMPORTS
# ============================================

import streamlit as st

from pages.intelligence_center.services.intelligence_center_service import (
    IntelligenceCenterService
)
from components.widgets.executive_banner import (
    ExecutiveBanner
)

from components.widgets.executive_kpi_strip import (
    ExecutiveKPIStrip
)

from components.widgets.recommendation_panel import (
    RecommendationPanel
)

from components.executive.executive_forecasts import (
    ExecutiveForecasts
)

from components.graphs.dependency_graph import (
    DependencyGraph
)

# ============================================
# PAGE
# ============================================

class IntelligenceCenterPage:

    def __init__(self):

        self.service = (
            IntelligenceCenterService()
        )

        self.snapshot = (
            self.service
            .get_intelligence_snapshot()
        )
    # ============================================
    # DEPENDENCY GRAPH
    # ============================================

    def render_dependency_graph(
        self
    ):

        st.subheader(
            "Dependency Intelligence"
        )

        graph_data = (
            self.service
            .get_dependency_graph()
        )

        DependencyGraph(
            graph_data
        ).render()


    # ============================================
    # PAGE RENDER
    # ============================================

    def render(self):

        ExecutiveBanner().render(

            title=
            "ICTA Intelligence Center",

            subtitle=
            "Cross-domain operational reasoning and intelligence"
        )

        ExecutiveKPIStrip().render(

            self.service.get_kpis()
        )

        st.markdown("---")

        self.render_signals()

        st.markdown("---")

        self.render_dependency_graph()

        st.markdown("---")

        self.render_forecasts()

        st.markdown("---")

        self.render_scenarios()

        st.markdown("---")

        self.render_recommendations()

    # ============================================
    # EXECUTIVE ASSESSMENT
    # ============================================

    def render_executive_assessment(
        self
    ):

        st.subheader(
            "Executive Assessment"
        )

        col1, col2, col3 = (
            st.columns(3)
        )

        with col1:

            st.metric(
                "Risk Level",
                self.snapshot.get(
                    "risk_level",
                    "unknown"
                ).upper()
            )

        with col2:

            st.metric(
                "System Status",
                self.snapshot.get(
                    "system_status",
                    "unknown"
                ).upper()
            )

        with col3:

            st.metric(
                "Critical Domains",
                len(
                    self.snapshot.get(
                        "critical_domains",
                        []
                    )
                )
            )

        observations = (
            self.snapshot.get(
                "observations",
                []
            )
        )

        for observation in observations:

            st.warning(
                observation
            )

    # ============================================
    # SIGNALS
    # ============================================

    def render_signals(
        self
    ):

        st.subheader(
            "Signal Intelligence"
        )

        signals = (
            self.snapshot.get(
                "signals",
                []
            )
        )

        if not signals:

            st.info(
                "No active signals detected."
            )

            return

        for signal in signals:

            st.success(
                signal
            )

    # ============================================
    # IMPACT SUMMARY
    # ============================================

    def render_impact_summary(
        self
    ):

        st.subheader(
            "Impact Intelligence"
        )

        summary = (
            self.snapshot.get(
                "impact_summary",
                {}
            )
        )

        col1, col2, col3 = (
            st.columns(3)
        )

        with col1:

            st.metric(
                "Impact Records",
                summary.get(
                    "impact_count",
                    0
                )
            )

        with col2:

            st.metric(
                "Affected Domains",
                summary.get(
                    "affected_domain_count",
                    0
                )
            )

        with col3:

            st.metric(
                "Risk Checkpoints",
                summary.get(
                    "high_risk_checkpoint_count",
                    0
                )
            )

        st.markdown(
            "### Affected Domains"
        )

        for domain in summary.get(
            "affected_domains",
            []
        ):

            st.write(
                f"• {domain}"
            )

        st.markdown(
            "### High Risk Checkpoints"
        )

        for checkpoint in summary.get(
            "high_risk_checkpoints",
            []
        ):

            st.write(
                f"• {checkpoint}"
            )

    # ============================================
    # FORECASTS
    # ============================================

    def render_forecasts(
        self
    ):

        st.subheader(
            "Forecast Intelligence"
        )

        forecasts = (
            self.snapshot.get(
                "forecasts",
                []
            )
        )

        if not forecasts:

            st.info(
                "No forecasts available."
            )

            return

        ExecutiveForecasts().render(
            forecasts
        )

    # ============================================
    # SCENARIOS
    # ============================================

    def render_scenarios(
        self
    ):

        st.subheader(
            "Scenario Intelligence"
        )

        scenarios = (
            self.snapshot.get(
                "scenarios",
                []
            )
        )

        if not scenarios:

            st.info(
                "No scenarios available."
            )

            return

        cols = st.columns(3)

        for i, scenario in enumerate(
            scenarios
        ):

            with cols[
                i % 3
            ]:

                st.info(

                    f"Scenario: "
                    f"{scenario.get('scenario')}\n\n"

                    f"Trigger: "
                    f"{scenario.get('trigger')}\n\n"

                    f"Response: "
                    f"{scenario.get('response')}"
                )

    # ============================================
    # RECOMMENDATIONS
    # ============================================

    def render_recommendations(
        self
    ):

        recommendations = []

        for rec in self.snapshot.get(
            "recommendations",
            []
        ):

            recommendations.append(

                f"[{rec['priority'].upper()}] "
                f"{rec['domain'].upper()} - "
                f"{rec['action']}"
            )

        RecommendationPanel().render(
            recommendations
        )

# ============================================
# ENTRY POINT
# ============================================

def render():

    page = (
        IntelligenceCenterPage()
    )

    page.render()
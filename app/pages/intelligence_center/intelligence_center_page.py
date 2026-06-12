import streamlit as st

from components.widgets.executive_banner import (
    ExecutiveBanner
)

from components.widgets.section_header import (
    SectionHeader
)

from components.graphs.dependency_graph import (
    DependencyGraph
)

from components.graphs.impact_graph import (
    ImpactGraph
)

from components.graphs.signal_flow_graph import (
    SignalFlowGraph
)

from components.graphs.domain_relationship_graph import (
    DomainRelationshipGraph
)

from pages.intelligence_center.services.intelligence_center_service import (
    IntelligenceCenterService
)


class IntelligenceCenterPage:

    def __init__(self):

        self.service = (
            IntelligenceCenterService()
        )

        self.banner = (
            ExecutiveBanner()
        )

        self.section_header = (
            SectionHeader()
        )

    def render(self):

        data = (
            self.service.get_data()
        )

        summary = data.get(
            "summary",
            {}
        )

        signals = data.get(
            "signals",
            []
        )

        impacts = data.get(
            "impacts",
            []
        )

        dependencies = data.get(
            "dependencies",
            {}
        )

        # ==========================================
        # BANNER
        # ==========================================

        self.banner.render(

            title=
            "ICTA Intelligence Center",

            subtitle=
            "Cross-Domain Dependency & Impact Intelligence"
        )

        st.markdown("---")

        # ==========================================
        # EXECUTIVE INTELLIGENCE OVERVIEW
        # ==========================================

        self.section_header.render(

            "Intelligence Overview",

            "Cross-domain intelligence derived from signals, impacts and dependencies."
        )

        col1, col2, col3, col4 = st.columns(4)

        with col1:

            st.metric(

                "Signals",

                summary.get(
                    "signal_count",
                    len(signals)
                )
            )

        with col2:

            st.metric(

                "High Risk",

                summary.get(
                    "high_risk_count",
                    0
                )
            )

        with col3:

            st.metric(

                "Impacts",

                summary.get(
                    "impact_count",
                    len(impacts)
                )
            )

        with col4:

            st.metric(

                "Dependencies",

                summary.get(
                    "dependency_count",
                    len(dependencies)
                )
            )

        st.markdown("---")

        # ==========================================
        # AI INTELLIGENCE BRIEF
        # ==========================================

        self.section_header.render(

            "Intelligence Brief",

            "AI-generated interpretation of active operational intelligence."
        )

        highest_location = summary.get(
            "highest_risk_location",
            "Unknown"
        )

        highest_score = summary.get(
            "highest_risk_score",
            0
        )

       

        # ==========================================
        # SIGNAL INTELLIGENCE
        # ==========================================

        self.section_header.render(

            "Signal Intelligence",

            "High-risk signals detected across operational domains."
        )

        SignalFlowGraph().render(
            signals
        )

        st.markdown("---")

        # ==========================================
        # DEPENDENCY INTELLIGENCE
        # ==========================================

        self.section_header.render(

            "Dependency Intelligence",

            "Cause-and-effect relationships across operational domains."
        )

        DependencyGraph(

            relationships=
            dependencies

        ).render()

        st.markdown("---")

        # ==========================================
        # IMPACT INTELLIGENCE
        # ==========================================

        self.section_header.render(

            "Impact Intelligence",

            "Projected downstream impacts from current operational conditions."
        )

        ImpactGraph().render(
            impacts
        )

        st.markdown("---")

        # ==========================================
        # DOMAIN RELATIONSHIPS
        # ==========================================

        self.section_header.render(

            "Domain Relationships",

            "Inter-domain connectivity and influence network."
        )

        DomainRelationshipGraph().render(
            impacts
        )
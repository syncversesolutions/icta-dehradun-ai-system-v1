import streamlit as st

from pages.traffic.services.traffic_service import (
    TrafficService
)

from components.graphs.dependency_graph import (
    DependencyGraph
)


class TrafficPage:

    def __init__(self):

        self.service = (
            TrafficService()
        )

    def render(self):

        summary = (
            self.service.get_summary()
        )

        st.title(
            "🚦 Traffic Operations Center"
        )

        st.caption(
            "Traffic intelligence and congestion management"
        )

        # =====================================
        # KPI STRIP
        # =====================================

        col1, col2, col3, col4 = (
            st.columns(4)
        )

        with col1:

            st.metric(
                "Congestion Score",
                f"{summary['congestion_score']}%"
            )

        with col2:

            st.metric(
                "Travel Time",
                summary[
                    "travel_time"
                ]
            )

        with col3:

            st.metric(
                "Throughput",
                summary[
                    "throughput"
                ]
            )

        with col4:

            st.metric(
                "Forecast Next Hour",
                f"{summary['forecast']}%"
            )

        # =====================================
        # EXECUTIVE ASSESSMENT
        # =====================================

        if summary["congestion_score"] >= 80:

            st.error(
                "Traffic network under severe congestion."
            )

        elif summary["congestion_score"] >= 50:

            st.warning(
                "Traffic pressure increasing."
            )

        else:

            st.success(
                "Traffic network operating normally."
            )

        st.divider()

        # =====================================
        # SIGNAL INTELLIGENCE
        # =====================================

        st.subheader(
            "Traffic Signal Intelligence"
        )

        signals = (
            self.service.get_signals()
        )

        if not signals:

            st.info(
                "No traffic signals detected."
            )

        else:

            for signal in signals:

                st.error(

                    f"{signal['checkpoint_name']} | "

                    f"{signal['risk_level']} | "

                    f"Score: "
                    f"{round(signal['predicted_score'],2)}"
                )

        st.divider()

        # =====================================
        # FORECAST INTELLIGENCE
        # =====================================

        st.subheader(
            "Forecast Intelligence"
        )

        predictions = (
            self.service.get_predictions()
        )

        if predictions.empty:

            st.info(
                "No forecast data available."
            )

        else:

            st.dataframe(

                predictions,

                use_container_width=True
            )

        st.divider()

        # =====================================
        # DEPENDENCY GRAPH
        # =====================================

        st.subheader(
            "Traffic Dependency Intelligence"
        )

        graph = (
            self.service
            .get_dependency_graph()
        )

        DependencyGraph(
            graph
        ).render()

        st.divider()

        # =====================================
        # RECOMMENDATIONS
        # =====================================

        st.subheader(
            "Operational Recommendations"
        )

        recommendations = (
            self.service
            .get_recommendations()
        )

        if not recommendations:

            st.info(
                "No traffic recommendations available."
            )

        else:

            for rec in recommendations:

                st.warning(

                    f"[{rec['priority'].upper()}] "

                    f"{rec['action']}"
                )
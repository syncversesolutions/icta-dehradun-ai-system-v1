import streamlit as st

from pages.accommodation.services.accommodation_service import (
    AccommodationService
)

from components.graphs.dependency_graph import (
    DependencyGraph
)


class AccommodationPage:

    def __init__(self):

        self.service = (
            AccommodationService()
        )

    def render(self):

        st.title(
            "🏨 Accommodation Operations Center"
        )

        st.caption(
            "Accommodation intelligence and occupancy optimization"
        )

        summary = (
            self.service.get_summary()
        )

        # =====================================
        # EXECUTIVE KPIS
        # =====================================

        col1, col2, col3, col4 = (
            st.columns(4)
        )

        with col1:

            st.metric(
                "Occupancy",
                f"{summary['occupancy']}%"
            )

        with col2:

            st.metric(
                "Available Beds",
                summary[
                    "available_beds"
                ]
            )

        with col3:

            st.metric(
                "Forecast 6h",
                f"{summary['forecast']}%"
            )

        with col4:

            st.metric(
                "Signals",
                summary[
                    "signals"
                ]
            )

        # =====================================
        # EXECUTIVE ASSESSMENT
        # =====================================

        if summary["occupancy"] >= 90:

            st.error(
                "Accommodation network approaching saturation."
            )

        elif summary["occupancy"] >= 80:

            st.warning(
                "Accommodation pressure increasing."
            )

        else:

            st.success(
                "Accommodation capacity healthy."
            )

        if summary["forecast"] >= 95:

            st.error(
                "Forecast indicates accommodation saturation within 6 hours."
            )

        st.divider()

        # =====================================
        # CAPACITY INTELLIGENCE
        # =====================================

        st.subheader(
            "Capacity Intelligence"
        )

        capacity = (
            self.service
            .get_capacity_summary()
        )

        if capacity:

            c1, c2, c3, c4 = (
                st.columns(4)
            )

            c1.metric(
                "Total Rooms",
                capacity[
                    "total_rooms"
                ]
            )

            c2.metric(
                "Occupied Rooms",
                capacity[
                    "occupied_rooms"
                ]
            )

            c3.metric(
                "Average Occupancy",
                f"{capacity['average_occupancy']}%"
            )

            c4.metric(
                "Peak Occupancy",
                f"{capacity['peak_occupancy']}%"
            )

        st.divider()

        # =====================================
        # SIGNAL INTELLIGENCE
        # =====================================

        st.subheader(
            "Accommodation Signals"
        )

        signals = (
            self.service.get_signals()
        )

        if not signals:

            st.info(
                "No accommodation signals found."
            )

        else:

            for signal in signals:

                signal_name = (
                    signal.get(
                        "signal",
                        "unknown"
                    )
                )

                value = (
                    signal.get(
                        "value",
                        0
                    )
                )

                status = (
                    signal.get(
                        "status",
                        "normal"
                    )
                )

                if status == "critical":

                    st.error(
                        f"{signal_name} | Value: {value}"
                    )

                elif status == "warning":

                    st.warning(
                        f"{signal_name} | Value: {value}"
                    )

                else:

                    st.success(
                        f"{signal_name} | Normal"
                    )

        st.divider()

        # =====================================
        # OPERATIONAL RECOMMENDATIONS
        # =====================================

        st.subheader(
            "Operational Recommendations"
        )

        if summary["occupancy"] > 90:

            st.warning(
                "Prepare overflow accommodation capacity."
            )

            st.warning(
                "Coordinate traffic rerouting strategy."
            )

            st.warning(
                "Increase crowd monitoring readiness."
            )

            st.warning(
                "Notify governance coordination team."
            )

        st.divider()

        # =====================================
        # FORECASTS
        # =====================================

        st.subheader(
            "Occupancy Forecasts"
        )

        predictions = (

            self.service
            .get_prediction_table()
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
        # DEPENDENCY INTELLIGENCE
        # =====================================

        st.subheader(
            "Accommodation Dependency Intelligence"
        )

        graph = (
            self.service
            .get_dependency_graph()
        )

        DependencyGraph(
            graph
        ).render()
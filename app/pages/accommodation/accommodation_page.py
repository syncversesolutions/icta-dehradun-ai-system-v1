import streamlit as st

from pages.accommodation.services.accommodation_service import (
    AccommodationService
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

        summary = (
            self.service.get_summary()
        )

        col1, col2, col3, col4 = st.columns(4)

        col1.metric(

            "Properties",

            summary[
                "properties"
            ]
        )

        col2.metric(

            "Accommodation Signals",

            summary[
                "signals"
            ]
        )

        col3.metric(

            "Average Occupancy",

            summary[
                "avg_occupancy"
            ]
        )

        col4.metric(

            "High Risk Events",

            summary[
                "high_risk"
            ]
        )

        st.divider()

        st.subheader(
            "Occupancy Predictions"
        )

        predictions = (

            self.service
            .get_prediction_table()
        )

        if predictions.empty:

            st.warning(
                "No accommodation predictions found."
            )

        else:

            st.dataframe(

                predictions,

                use_container_width=True
            )

        st.divider()

        st.subheader(
            "Accommodation Signals"
        )

        signals = (
            self.service.get_signals()
        )

        if len(signals) == 0:

            st.info(
                "No active accommodation signals"
            )

        else:

            st.json(
                signals
            )

        st.divider()

        st.subheader(
            "Global System State"
        )

        state = summary.get(
            "state",
            {}
        )

        st.json(
            state
        )
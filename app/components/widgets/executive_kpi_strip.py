import streamlit as st


class ExecutiveKPIStrip:

    def __init__(self):
        pass

    def render(
        self,
        summary
    ):

        risk = summary.get(
            "risk_level",
            "UNKNOWN"
        )

        signals = summary.get(
            "active_signals",
            0
        )

        forecasts = summary.get(
            "forecast_count",
            0
        )

        actions = summary.get(
            "autonomous_actions",
            0
        )

        col1, col2, col3, col4 = st.columns(4)

        with col1:

            st.metric(
                "Risk Level",
                risk
            )

        with col2:

            st.metric(
                "Active Signals",
                signals
            )

        with col3:

            st.metric(
                "Forecasts",
                forecasts
            )

        with col4:

            st.metric(
                "Autonomous Actions",
                actions
            )
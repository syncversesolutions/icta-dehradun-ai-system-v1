import streamlit as st


class AutonomyMonitor:

    def __init__(self):
        pass

    def render(
        self,
        actions,
        recoveries
    ):

        col1, col2 = st.columns(2)

        with col1:

            st.metric(
                "Actions",
                actions
            )

        with col2:

            st.metric(
                "Recoveries",
                recoveries
            )
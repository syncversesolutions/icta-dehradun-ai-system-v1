import streamlit as st


class SignalSummary:

    def __init__(self):
        pass

    def render(
        self,
        signals
    ):

        st.markdown(
            "### Active Signals"
        )

        st.metric(
            "Signals",
            len(signals)
        )
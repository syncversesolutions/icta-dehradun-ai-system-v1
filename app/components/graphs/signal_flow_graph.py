import streamlit as st


class SignalFlowGraph:

    def __init__(self):
        pass

    def render(
        self,
        signals
    ):

        st.subheader(
            "Signal Flow"
        )

        st.info(
            f"{len(signals)} active signals flowing through system"
        )
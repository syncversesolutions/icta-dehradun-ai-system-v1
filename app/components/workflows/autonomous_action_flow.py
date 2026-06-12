import streamlit as st


class AutonomousActionFlow:

    def __init__(self):
        pass

    def render(
        self,
        actions
    ):

        st.success(
            f"{len(actions)} autonomous actions executed"
        )
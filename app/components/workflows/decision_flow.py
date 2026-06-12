import streamlit as st


class DecisionFlow:

    def __init__(self):
        pass

    def render(
        self,
        decisions
    ):

        for decision in decisions:

            st.write(decision)
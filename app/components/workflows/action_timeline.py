import streamlit as st


class ActionTimeline:

    def __init__(self):
        pass

    def render(
        self,
        actions
    ):

        for action in actions:

            st.markdown(
                f"• {action}"
            )
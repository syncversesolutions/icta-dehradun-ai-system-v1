import streamlit as st


class MemoryActivity:

    def __init__(self):
        pass

    def render(
        self,
        episodes
    ):

        st.metric(
            "Memory Episodes",
            len(episodes)
        )
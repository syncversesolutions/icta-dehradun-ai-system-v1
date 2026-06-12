import streamlit as st


class AgentActivity:

    def __init__(self):
        pass

    def render(
        self,
        agents
    ):

        st.metric(
            "Active Agents",
            len(agents)
        )
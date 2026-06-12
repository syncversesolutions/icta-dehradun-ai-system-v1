import streamlit as st


class PipelineHealth:

    def __init__(self):
        pass

    def render(
        self,
        status
    ):

        st.metric(
            "Pipeline Health",
            status
        )
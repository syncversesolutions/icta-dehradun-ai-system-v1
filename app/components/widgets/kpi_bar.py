import streamlit as st


class KPIBar:

    def __init__(self):
        pass

    def render(
        self,
        metrics
    ):

        cols = st.columns(
            len(metrics)
        )

        for col, metric in zip(
            cols,
            metrics
        ):

            with col:

                st.metric(

                    metric["title"],

                    metric["value"]
                )
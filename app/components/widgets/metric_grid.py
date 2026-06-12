import streamlit as st


class MetricGrid:

    @staticmethod
    def render(
        metrics
    ):

        cols = st.columns(
            len(metrics)
        )

        for i, metric in enumerate(
            metrics
        ):

            with cols[i]:

                st.metric(
                    metric["label"],
                    metric["value"]
                )
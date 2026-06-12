import streamlit as st
import pandas as pd


class SystemMetrics:

    def __init__(self):
        pass

    # ========================================
    # RENDER
    # ========================================

    def render(
        self,
        metrics
    ):

        st.subheader(
            "System Metrics"
        )

        if not metrics:

            st.info(
                "No metrics available"
            )

            return

        if isinstance(
            metrics,
            dict
        ):

            dataframe = pd.DataFrame(
                [metrics]
            )

        else:

            dataframe = pd.DataFrame(
                metrics
            )

        st.dataframe(

            dataframe,

            use_container_width=True
        )
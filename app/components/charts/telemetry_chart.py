import streamlit as st

import pandas as pd


class TelemetryChart:

    def __init__(

        self,
        metrics

    ):

        self.metrics = metrics

    # ========================================
    # RENDER
    # ========================================

    def render(self):

        st.subheader(
            "System Telemetry"
        )

        if len(self.metrics) == 0:

            st.info(
                "No telemetry metrics"
            )

            return

        dataframe = pd.DataFrame(
            self.metrics
        )

        st.line_chart(
            dataframe
        )
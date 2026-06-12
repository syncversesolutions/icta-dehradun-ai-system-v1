import streamlit as st
import pandas as pd
class AlertTable:
    def __init__(
        self,
        alerts
    ):
        self.alerts = alerts
    # ========================================
    # RENDER
    # ========================================
    def render(self):
        st.subheader(
            "Operational Alerts"
        )
        # ====================================
        # EMPTY DATA
        # ====================================
        if len(self.alerts) == 0:
            st.info(
                "No alerts available"
            )
            return
        # ====================================
        # DATAFRAME
        # ====================================
        dataframe = pd.DataFrame(
            self.alerts
        )
        st.dataframe(
            dataframe,
            use_container_width=True
        )
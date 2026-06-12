import streamlit as st
import pandas as pd
import plotly.express as px


class RiskDistributionChart:

    def __init__(self):
        pass

    def render(
        self,
        signals
    ):

        if len(signals) == 0:

            return

        df = pd.DataFrame(signals)

        fig = px.pie(

            df,

            names="risk_level",

            title="Risk Distribution"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )
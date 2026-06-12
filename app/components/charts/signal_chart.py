import streamlit as st
import pandas as pd
import plotly.express as px

from components.base.base_chart import (
    BaseChart
)


class SignalChart(BaseChart):

    def __init__(self):

        super()._init_()

    def render(
        self,
        signals
    ):

        if len(signals) == 0:

            st.info(
                "No signals available"
            )

            return

        df = pd.DataFrame(signals)

        fig = px.histogram(

            df,

            x="signal_type",

            color="risk_level",

            title="Signal Distribution"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )
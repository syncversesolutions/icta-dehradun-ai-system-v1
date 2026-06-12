import streamlit as st
import pandas as pd
import plotly.express as px

from components.base.base_chart import (
    BaseChart
)


class PredictionChart(BaseChart):

    def __init__(self):

        super()._init_()

    def render(
        self,
        dataframe
    ):

        if dataframe.empty:

            st.info(
                "No prediction data available"
            )

            return

        fig = px.line(

            dataframe,

            x="route_id",

            y="predicted_congestion_score",

            markers=True,

            title="Traffic Predictions"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )
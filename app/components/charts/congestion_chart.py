import streamlit as st
import plotly.express as px

from components.base.base_chart import (
    BaseChart
)


class CongestionChart(BaseChart):

    def __init__(self):

        super()._init_()

    def render(
        self,
        dataframe
    ):

        fig = px.bar(

            dataframe,

            x="checkpoint_name",

            y="vehicle_count",

            color="congestion_level",

            title="Checkpoint Congestion"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )
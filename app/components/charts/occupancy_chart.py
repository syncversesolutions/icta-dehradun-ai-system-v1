import streamlit as st
import pandas as pd
import plotly.express as px


class OccupancyChart:

    def __init__(self):
        pass

    def render(
        self,
        dataframe
    ):

        if dataframe.empty:

            return

        fig = px.bar(

            dataframe,

            x="property_name",

            y="occupancy_rate",

            title="Accommodation Occupancy"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )
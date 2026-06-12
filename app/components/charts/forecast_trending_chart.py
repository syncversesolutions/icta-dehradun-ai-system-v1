import streamlit as st
import pandas as pd
import plotly.express as px


class ForecastTrendChart:

    def __init__(self):
        pass

    def render(
        self,
        forecasts
    ):

        if len(forecasts) == 0:

            return

        df = pd.DataFrame(forecasts)

        fig = px.bar(

            df,

            x="forecast",

            y="probability",

            title="Forecast Probability"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )
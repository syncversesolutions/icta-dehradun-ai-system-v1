import streamlit as st
import pandas as pd


class ForecastTable:

    def __init__(self):
        pass

    def render(
        self,
        forecasts
    ):

        df = pd.DataFrame(forecasts)

        st.dataframe(
            df,
            use_container_width=True
        )
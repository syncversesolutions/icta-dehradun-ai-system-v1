import streamlit as st
import pandas as pd


class RecommendationTable:

    def __init__(self):
        pass

    def render(
        self,
        recommendations
    ):

        df = pd.DataFrame(
            recommendations
        )

        st.dataframe(
            df,
            use_container_width=True
        )
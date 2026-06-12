import streamlit as st
import plotly.express as px
import pandas as pd


class BaseChart:

    def __init__(self):
        pass

    def render_bar(
        self,
        dataframe,
        x,
        y,
        title=""
    ):

        fig = px.bar(
            dataframe,
            x=x,
            y=y,
            title=title
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    def render_line(
        self,
        dataframe,
        x,
        y,
        title=""
    ):

        fig = px.line(
            dataframe,
            x=x,
            y=y,
            title=title
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )
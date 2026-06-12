import streamlit as st
import pandas as pd


class BaseTable:

    def __init__(self):
        pass

    def render(
        self,
        dataframe
    ):

        st.dataframe(
            dataframe,
            use_container_width=True
        )
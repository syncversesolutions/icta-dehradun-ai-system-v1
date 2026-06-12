import streamlit as st
import pandas as pd


class SignalTable:

    def __init__(self):
        pass

    def render(
        self,
        signals
    ):

        df = pd.DataFrame(signals)

        st.dataframe(
            df,
            use_container_width=True
        )
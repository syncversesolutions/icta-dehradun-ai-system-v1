import streamlit as st


class RecoveryFlow:

    def __init__(self):
        pass

    def render(
        self,
        recoveries
    ):

        st.info(
            f"{recoveries} recoveries completed"
        )
import streamlit as st
import pandas as pd


class WorkflowTable:

    def __init__(self):
        pass

    def render(
        self,
        workflows
    ):

        df = pd.DataFrame(workflows)

        st.dataframe(
            df,
            use_container_width=True
        )
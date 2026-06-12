import streamlit as st
import pandas as pd
import plotly.express as px


class WorkflowExecutionChart:

    def __init__(self):
        pass

    def render(
        self,
        workflows
    ):

        if len(workflows) == 0:

            return

        df = pd.DataFrame(workflows)

        fig = px.histogram(

            df,

            x="status",

            title="Workflow Status"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )
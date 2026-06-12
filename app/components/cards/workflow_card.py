import streamlit as st

from components.base.base_card import (
    BaseCard
)


class WorkflowCard(BaseCard):

    def __init__(self):

        super()._init_()

    def render(
        self,
        workflow
    ):

        st.markdown(
            f"""
            <div class="icta-card">

            <h4>
            {workflow.get('workflow')}
            </h4>

            <p>
            Status:
            {workflow.get('status')}
            </p>

            </div>
            """,
            unsafe_allow_html=True
        )
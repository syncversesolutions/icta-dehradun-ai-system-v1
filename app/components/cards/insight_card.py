import streamlit as st

from components.base.base_card import (
    BaseCard
)


class InsightCard(BaseCard):

    def __init__(self):

        super()._init_()

    def render(
        self,
        insight
    ):

        st.markdown(
            f"""
            <div class="icta-card">

            <strong>
            Insight
            </strong>

            <br>

            {insight}

            </div>
            """,
            unsafe_allow_html=True
        )
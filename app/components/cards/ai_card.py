import streamlit as st

from components.base.base_card import (
    BaseCard
)


class AICard(BaseCard):

    def __init__(self):

        super()._init_()

    def render(
        self,
        title,
        recommendation
    ):

        st.markdown(
            f"""
            <div class="icta-card">

            <h4>
            {title}
            </h4>

            <p>
            {recommendation}
            </p>

            </div>
            """,
            unsafe_allow_html=True
        )
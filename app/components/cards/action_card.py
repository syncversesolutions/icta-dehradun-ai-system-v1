import streamlit as st

from components.base.base_card import (
    BaseCard
)


class ActionCard(BaseCard):

    def __init__(self):

        super()._init_()

    def render(
        self,
        action
    ):

        st.markdown(
            f"""
            <div class="icta-success">

            {action}

            </div>
            """,
            unsafe_allow_html=True
        )
import streamlit as st

from components.base.base_card import (
    BaseCard
)


class DomainCard(BaseCard):

    def __init__(self):

        super()._init_()

    def render(
        self,
        domain,
        status
    ):

        st.markdown(
            f"""
            <div class="icta-card">

            <h4>{domain}</h4>

            <p>{status}</p>

            </div>
            """,
            unsafe_allow_html=True
        )
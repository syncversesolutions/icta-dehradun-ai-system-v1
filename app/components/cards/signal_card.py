import streamlit as st

from components.base.base_card import (
    BaseCard
)


class SignalCard(BaseCard):

    def __init__(self):

        super()._init_()

    def render(
        self,
        signal
    ):

        st.markdown(
            f"""
            <div class="icta-card">

            <h4>
            {signal.get('signal_type','Unknown')}
            </h4>

            <p>
            Domain:
            {signal.get('domain','Unknown')}
            </p>

            <p>
            Risk:
            {signal.get('risk_level','Unknown')}
            </p>

            </div>
            """,
            unsafe_allow_html=True
        )
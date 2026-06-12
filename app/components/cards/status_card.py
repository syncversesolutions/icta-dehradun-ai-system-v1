import streamlit as st

from components.base.base_card import (
    BaseCard
)


class StatusCard(BaseCard):

    def __init__(self):

        super()._init_()

    def render(
        self,
        title,
        status
    ):

        color = "#22C55E"

        if str(status).lower() in [
            "warning",
            "medium"
        ]:
            color = "#F59E0B"

        if str(status).lower() in [
            "critical",
            "high"
        ]:
            color = "#EF4444"

        st.markdown(
            f"""
            <div class="icta-card">

                <div class="icta-card-title">
                    {title}
                </div>

                <h2 style="color:{color};">
                    {status}
                </h2>

            </div>
            """,
            unsafe_allow_html=True
        )
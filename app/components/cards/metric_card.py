import streamlit as st

from components.base.base_card import (
    BaseCard
)


class MetricCard(BaseCard):

    def __init__(self):

        super()._init_()

    def render(
        self,
        title,
        value,
        subtitle=""
    ):

        st.markdown(
            f"""
            <div class="icta-card">

                <div class="icta-card-title">
                    {title}
                </div>

                <div class="icta-card-value">
                    {value}
                </div>

                <div style="color:#94A3B8;">
                    {subtitle}
                </div>

            </div>
            """,
            unsafe_allow_html=True
        )
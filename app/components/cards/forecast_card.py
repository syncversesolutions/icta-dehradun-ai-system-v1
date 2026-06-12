import streamlit as st

from components.base.base_card import (
    BaseCard
)


class ForecastCard(BaseCard):

    def __init__(self):

        super()._init_()

    def render(
        self,
        forecast
    ):

        probability = (
            forecast.get(
                "probability",
                0
            ) * 100
        )

        st.markdown(
            f"""
            <div class="icta-card">

            <h4>
            {forecast.get('forecast')}
            </h4>

            <h2>
            {probability:.0f}%
            </h2>

            <p>
            {forecast.get('expected_impact')}
            </p>

            </div>
            """,
            unsafe_allow_html=True
        )
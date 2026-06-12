import streamlit as st


class ForecastSummary:

    def __init__(self):
        pass

    def render(
        self,
        forecasts
    ):

        st.subheader(
            "Forecast Summary"
        )

        for forecast in forecasts:

            st.info(

                f"{forecast.get('forecast')}"

                f" | "

                f"{forecast.get('expected_impact')}"
            )
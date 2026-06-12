import streamlit as st

from pages.scenario_lab.services.scenario_lab_service import (
    ScenarioLabService
)


class ScenarioLabPage:

    def __init__(self):

        self.service = (
            ScenarioLabService()
        )

    def render(self):

        st.title(
            "🧪 Scenario Lab"
        )

        scenarios = (
            self.service
            .get_scenarios()
        )

        for item in scenarios:

            with st.expander(

                item["scenario"]
            ):

                st.write(
                    item["trigger"]
                )

                st.success(
                    item["response"]
                )
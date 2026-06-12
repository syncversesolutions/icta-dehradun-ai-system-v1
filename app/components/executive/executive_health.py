import streamlit as st

from components.widgets.health_indicator import (
    HealthIndicator
)

from components.widgets.risk_indicator import (
    RiskIndicator
)


class ExecutiveHealth:

    def __init__(self):

        self.health = (
            HealthIndicator()
        )

        self.risk = (
            RiskIndicator()
        )

    def render(
        self,
        state
    ):

        col1, col2 = st.columns(2)

        with col1:

            self.health.render(
                state.get(
                    "system_status",
                    "Unknown"
                )
            )

        with col2:

            self.risk.render(
                state.get(
                    "risk_level",
                    "Unknown"
                )
            )
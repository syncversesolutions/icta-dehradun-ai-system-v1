import streamlit as st

from components.base.base_card import (
    BaseCard
)


class AlertCard(BaseCard):

    def __init__(self):

        super()._init_()

    def render(
        self,
        alert
    ):

        st.markdown(
            f"""
            <div class="icta-alert">

            <strong>
            {alert}
            </strong>

            </div>
            """,
            unsafe_allow_html=True
        )import streamlit as st


class AlertCard:

    def __init__(

        self,
        source_signal,
        severity,
        timestamp=None

    ):

        self.source_signal = (
            source_signal
        )

        self.severity = severity

        self.timestamp = timestamp

    # ========================================
    # GET ALERT COLOR
    # ========================================

    def get_alert_style(self):

        severity = (
            self.severity.upper()
        )

        if severity == "LOW":

            return "🟢"

        elif severity == "MEDIUM":

            return "🟠"

        elif severity == "HIGH":

            return "🔴"

        elif severity == "SEVERE":

            return "🚨"

        return "⚪"

    # ========================================
    # RENDER ALERT
    # ========================================

    def render(self):

        icon = self.get_alert_style()

        st.warning(

            f"{icon} "

            f"{self.source_signal} "

            f"({self.severity})"
        )

        if self.timestamp:

            st.caption(
                self.timestamp
            )
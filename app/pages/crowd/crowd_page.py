import streamlit as st

from pages.crowd.services.crowd_service import (
    CrowdService
)


class CrowdPage:

    def __init__(self):

        self.service = (
            CrowdService()
        )

    def render(self):

        st.title(
            "👥 Crowd Operations Center"
        )

        summary = (
            self.service.get_summary()
        )

        col1, col2, col3, col4 = st.columns(4)

        col1.metric(

            "Crowd Signals",

            summary[
                "crowd_signals"
            ]
        )

        col2.metric(

            "Impact Chains",

            summary[
                "impact_count"
            ]
        )

        col3.metric(

            "Risk Level",

            summary[
                "risk_level"
            ]
        )

        col4.metric(

            "Critical Domains",

            summary[
                "critical_domains"
            ]
        )

        st.divider()

        st.subheader(
            "Crowd Intelligence"
        )

        impacts = (
            self.service.get_impacts()
        )

        if len(impacts) == 0:

            st.info(
                "No crowd impacts detected"
            )

        else:

            st.json(
                impacts
            )

        st.divider()

        st.subheader(
            "Signal Layer"
        )

        signals = (
            self.service.get_signals()
        )

        st.json(
            signals
        )

        st.divider()

        st.subheader(
            "Current State"
        )

        state = (
            self.service.get_state()
        )

        st.json(
            state
        )
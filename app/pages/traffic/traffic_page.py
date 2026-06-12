import streamlit as st

from layouts.domain_layout import (
    DomainLayout
)

from pages.traffic.services.traffic_service import (
    TrafficService
)


class TrafficPage:

    def __init__(self):

        self.layout = (
            DomainLayout()
        )

        self.service = (
            TrafficService()
        )

    def render(self):

        data = (
            self.service.get_data()
        )

        self.layout.render(

            header=lambda:
                st.title(
                    "Traffic Domain"
                ),

            kpis=lambda:
                st.write(
                    "Traffic KPIs"
                ),

            charts=lambda:
                st.write(
                    "Traffic Charts"
                ),

            signals=lambda:
                st.write(
                    "Traffic Signals"
                ),

            recommendations=lambda:
                st.write(
                    "Traffic Recommendations"
                )
        )
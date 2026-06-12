import streamlit as st

from components.widgets.executive_banner import (
    ExecutiveBanner
)

from components.telemetry.runtime_health import (
    RuntimeHealth
)

from components.telemetry.system_metrics import (
    SystemMetrics
)

from components.telemetry.execution_trace import (
    ExecutionTrace
)

from pages.observability.services.observability_service import (
    ObservabilityService
)


class ObservabilityPage:

    def __init__(self):

        self.service = (
            ObservabilityService()
        )

        self.banner = (
            ExecutiveBanner()
        )

        self.runtime_health = (
            RuntimeHealth()
        )

        self.system_metrics = (
            SystemMetrics()
        )

        self.execution_trace = (
            ExecutionTrace()
        )

    def render(self):

        data = (
            self.service.get_data()
        )

        self.banner.render(

            title=
                "Platform Observability",

            subtitle=
                "Runtime Health, Telemetry & System Monitoring"
        )

        st.markdown("---")

        col1, col2 = st.columns(2)

        with col1:

            self.runtime_health.render(
                data
            )

        with col2:

            self.system_metrics.render(
                data
            )

        st.markdown("---")

        self.execution_trace.render(
            data
        )
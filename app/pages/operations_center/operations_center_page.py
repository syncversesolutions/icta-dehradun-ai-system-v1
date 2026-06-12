import streamlit as st

from components.widgets.executive_banner import (
    ExecutiveBanner
)

from components.charts.workflow_execution_chart import (
    WorkflowExecutionChart
)

from components.workflows.autonomous_action_flow import (
    AutonomousActionFlow
)

from components.workflows.recovery_flow import (
    RecoveryFlow
)

from components.workflows.action_timeline import (
    ActionTimeline
)

from pages.operations_center.services.operations_center_service import (
    OperationsCenterService
)


class OperationsCenterPage:

    def __init__(self):

        self.service = (
            OperationsCenterService()
        )

        self.banner = (
            ExecutiveBanner()
        )

        self.workflow_chart = (
            WorkflowExecutionChart()
        )

        self.action_flow = (
            AutonomousActionFlow()
        )

        self.recovery_flow = (
            RecoveryFlow()
        )

        self.timeline = (
            ActionTimeline()
        )

    def render(self):

        data = (
            self.service.get_data()
        )

        autonomy = data["autonomy"]

        workflows = data["workflows"]

        self.banner.render(

            title=
                "Operations Center",

            subtitle=
                "Autonomous Execution & Workflow Intelligence"
        )

        st.markdown("---")

        self.workflow_chart.render(
            workflows
        )

        st.markdown("---")

        self.action_flow.render(

            autonomy.get(
                "execution_logs",
                []
            )
        )

        st.markdown("---")

        self.recovery_flow.render(

            autonomy.get(
                "recoveries",
                0
            )
        )

        st.markdown("---")

        self.timeline.render(

            autonomy.get(
                "execution_logs",
                []
            )
        )
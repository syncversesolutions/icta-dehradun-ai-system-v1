import streamlit as st


class WorkflowTimeline:

    def __init__(

        self,
        workflows

    ):

        self.workflows = workflows

    # ========================================
    # RENDER
    # ========================================

    def render(self):

        st.subheader(
            "Workflow Timeline"
        )

        if len(self.workflows) == 0:

            st.info(
                "No workflows available"
            )

            return

        for workflow in self.workflows:

            st.write(

                f"• {workflow}"
            )
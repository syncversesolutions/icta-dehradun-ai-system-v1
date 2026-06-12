import streamlit as st


class OrchestrationFlow:

    def __init__(

        self,
        actions

    ):

        self.actions = actions

    # ========================================
    # RENDER
    # ========================================

    def render(self):

        st.subheader(
            "Orchestration Flow"
        )

        if len(self.actions) == 0:

            st.info(
                "No orchestration actions"
            )

            return

        for index, action in enumerate(
            self.actions,
            start=1
        ):

            st.write(

                f"{index}. {action}"
            )
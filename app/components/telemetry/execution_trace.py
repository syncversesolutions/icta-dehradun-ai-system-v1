import streamlit as st


class ExecutionTrace:

    def __init__(self):
        pass

    def render(
        self,
        state
    ):

        st.subheader(
            "Execution Trace"
        )

        artifacts = state.get(
            "artifacts_generated",
            []
        )

        if not artifacts:

            st.info(
                "No execution history available"
            )

            return

        for artifact in artifacts:

            st.success(
                f"✓ {artifact}"
            )
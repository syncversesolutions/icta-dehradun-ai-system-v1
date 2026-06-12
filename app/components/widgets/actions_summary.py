import streamlit as st


class ActionSummary:

    def __init__(self):
        pass

    def render(
        self,
        actions
    ):

        st.subheader(
            "Autonomous Actions"
        )

        if not actions:

            st.info(
                "No actions executed"
            )

            return

        for action in actions:

            if isinstance(
                action,
                dict
            ):

                st.success(

                    action.get(
                        "action",
                        "Unknown"
                    )
                )

            else:

                st.success(
                    str(action)
                )
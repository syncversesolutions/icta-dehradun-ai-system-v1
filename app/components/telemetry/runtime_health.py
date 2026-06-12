import streamlit as st


class RuntimeHealth:

    def __init__(self):
        pass

    # ========================================
    # RENDER
    # ========================================

    def render(
        self,
        health_data
    ):

        st.subheader(
            "Runtime Health"
        )

        system_status = health_data.get(
            "system_status",
            "UNKNOWN"
        )

        if str(system_status).upper() == "ACTIVE":

            st.success(
                f"System Status: {system_status}"
            )

        else:

            st.warning(
                f"System Status: {system_status}"
            )

        st.json(
            health_data
        )
import streamlit as st


class HealthIndicator:

    def __init__(self):
        pass

    def render(
        self,
        status
    ):

        color = "#22C55E"

        if status.lower() == "warning":

            color = "#F59E0B"

        if status.lower() == "critical":

            color = "#EF4444"

        st.markdown(
            f"""
            <div class="icta-card">

                <h4>
                    System Health
                </h4>

                <h2 style="
                    color:{color};
                ">
                    {status}
                </h2>

            </div>
            """,
            unsafe_allow_html=True
        )
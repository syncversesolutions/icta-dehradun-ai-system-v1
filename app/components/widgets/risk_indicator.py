import streamlit as st


class RiskIndicator:

    def __init__(self):
        pass

    def render(
        self,
        risk_level
    ):

        color = "#22C55E"

        if risk_level.lower() == "medium":

            color = "#F59E0B"

        if risk_level.lower() == "high":

            color = "#EF4444"

        st.markdown(
            f"""
            <div class="icta-card">

                <h4>
                    Risk Level
                </h4>

                <h2 style="
                    color:{color};
                ">
                    {risk_level}
                </h2>

            </div>
            """,
            unsafe_allow_html=True
        )
import streamlit as st


class ExecutiveLayout:

    def __init__(self):
        pass

    def render(

        self,

        banner,

        kpis,

        health,

        signals,

        forecasts,

        actions,

        recommendations
    ):

        banner()

        st.markdown("---")

        kpis()

        st.markdown("---")

        health()

        st.markdown("---")

        signals()

        st.markdown("---")

        forecasts()

        st.markdown("---")

        actions()

        st.markdown("---")

        recommendations()
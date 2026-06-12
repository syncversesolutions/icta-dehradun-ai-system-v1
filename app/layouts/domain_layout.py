import streamlit as st


class DomainLayout:

    def __init__(self):
        pass

    def render(

        self,

        header,

        kpis,

        charts,

        signals,

        recommendations
    ):

        header()

        st.markdown("---")

        kpis()

        st.markdown("---")

        charts()

        st.markdown("---")

        signals()

        st.markdown("---")

        recommendations()
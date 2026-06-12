import streamlit as st


class BaseWidget:

    def __init__(self):
        pass

    def section_header(
        self,
        title,
        subtitle=""
    ):

        st.markdown(
            f"""
            <div class="icta-card">

            <h3>{title}</h3>

            <p>{subtitle}</p>

            </div>
            """,
            unsafe_allow_html=True
        )
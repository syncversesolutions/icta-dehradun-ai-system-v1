import streamlit as st


class BaseCard:

    def __init_(self):
        pass

    def start(self):

        st.markdown(
            """
            <div class="icta-card">
            """,
            unsafe_allow_html=True
        )

    def end(self):

        st.markdown(
            """
            </div>
            """,
            unsafe_allow_html=True
        )

    def render_title(
        self,
        title
    ):

        st.markdown(
            f"""
            <div class="icta-card-title">
            {title}
            </div>
            """,
            unsafe_allow_html=True
        )
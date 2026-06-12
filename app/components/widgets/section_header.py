import streamlit as st


class SectionHeader:

    def __init__(self):
        pass

    def render(
        self,
        title,
        subtitle=""
    ):

        st.markdown(
            f"## {title}"
        )

        if subtitle:

            st.caption(
                subtitle
            )
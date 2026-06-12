import streamlit as st


class Header:

    def __init__(

        self,
        title,
        subtitle=None

    ):

        self.title = title

        self.subtitle = subtitle

    # ========================================
    # RENDER
    # ========================================

    def render(self):

        st.title(
            self.title
        )

        if self.subtitle:

            st.caption(
                self.subtitle
            )

        st.markdown("---")
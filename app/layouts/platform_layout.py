import streamlit as st


class PlatformLayout:

    def __init__(self):
        pass

    def render(

        self,

        title,

        body
    ):

        st.markdown(
            f"""
            <div style="
                padding-bottom:20px;
            ">
                <h1>
                    {title}
                </h1>
            </div>
            """,
            unsafe_allow_html=True
        )

        body()
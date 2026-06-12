import streamlit as st


class LightTheme:

    def apply(self):

        st.markdown(

            """
            <style>

            .stApp {

                background-color: white;

                color: black;
            }

            </style>
            """,

            unsafe_allow_html=True
        )
from pathlib import Path
import streamlit as st


class ThemeLoader:

    @staticmethod
    def load():

        styles = ""

        css_files = [

            "cards.css",
            "dashboards.css",
            "metrics.css",
            "executive.css",
            "graphs.css"
        

        ]

        for css_file in css_files:

            path = (
                Path(__file__).parent /
                css_file
            )

            if path.exists():

                styles += path.read_text(
                    encoding="utf-8"
                )

        if styles:

            st.markdown(
                f"""
                <style>
                {styles}
                </style>
                """,
                unsafe_allow_html=True
            )
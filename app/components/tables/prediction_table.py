import streamlit as st

import pandas as pd


class PredictionTable:

    def __init__(

        self,
        predictions

    ):

        self.predictions = predictions

    # ========================================
    # RENDER
    # ========================================

    def render(self):

        if len(self.predictions) == 0:

            st.info(
                "No predictions available"
            )

            return

        dataframe = pd.DataFrame(
            self.predictions
        )

        st.dataframe(

            dataframe,

            use_container_width=True
        )
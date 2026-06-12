import streamlit as st
import pandas as pd
class TrafficMap:
    def __init__(
        self,
        coordinates
    ):
        self.coordinates = (
            coordinates
        )
    # ========================================
    # RENDER
    # ========================================
    def render(self):
        st.subheader(
            "Traffic Intelligence Map"
        )
        # ====================================
        # EMPTY DATA
        # ====================================
        if len(self.coordinates) == 0:
            st.info(
                "No map coordinates available"
            )
            return
        # ====================================
        # DATAFRAME
        # ====================================
        dataframe = pd.DataFrame(
            self.coordinates
        )
        # ====================================
        # MAP
        # ====================================
        st.map(
            dataframe
        )
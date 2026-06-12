import streamlit as st
import networkx as nx
import plotly.graph_objects as go


class BaseGraph:

    def __init__(self):
        pass

    def render_placeholder(
        self,
        title
    ):

        st.info(
            f"{title} graph ready"
        )
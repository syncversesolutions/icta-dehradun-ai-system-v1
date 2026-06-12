import streamlit as st
import networkx as nx
import plotly.graph_objects as go


class DependencyGraph:

    def __init__(
        self,
        relationships=None
    ):

        self.relationships = (
            relationships or {}
        )

    def build_graph(self):

        graph = nx.DiGraph()

        for source, config in (

            self.relationships.items()

        ):

            targets = config.get(
                "affects",
                []
            )

            for target in targets:

                graph.add_edge(
                    source,
                    target
                )

        return graph

    def render(self):

        graph = self.build_graph()

        if len(
            graph.nodes()
        ) == 0:

            st.info(
                "No dependency data available."
            )

            return

        pos = nx.spring_layout(

            graph,

            seed=42,

            k=1.5
        )

        edge_x = []
        edge_y = []

        for edge in graph.edges():

            x0, y0 = pos[
                edge[0]
            ]

            x1, y1 = pos[
                edge[1]
            ]

            edge_x.extend(
                [x0, x1, None]
            )

            edge_y.extend(
                [y0, y1, None]
            )

        edge_trace = go.Scatter(

            x=edge_x,

            y=edge_y,

            mode="lines",

            hoverinfo="none",

            line=dict(
                width=2
            )
        )

        node_x = []
        node_y = []
        node_text = []

        for node in graph.nodes():

            x, y = pos[node]

            node_x.append(x)

            node_y.append(y)

            node_text.append(node)

        node_trace = go.Scatter(

            x=node_x,

            y=node_y,

            mode="markers+text",

            text=node_text,

            textposition=
            "bottom center",

            marker=dict(
                size=28
            )
        )

        fig = go.Figure(

            data=[
                edge_trace,
                node_trace
            ]
        )

        fig.update_layout(

            title=
            "Cross-Domain Dependency Graph",

            showlegend=False,

            height=700
        )

        st.plotly_chart(

            fig,

            use_container_width=True
        )
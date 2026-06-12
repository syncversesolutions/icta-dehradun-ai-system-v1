import streamlit as st
import plotly.graph_objects as go


class ImpactGraph:

    def __init__(self):
        pass

    def render(
        self,
        impacts
    ):

        if not impacts:

            st.info(
                "No impacts available"
            )

            return

        sources = []
        targets = []

        labels = []

        for impact in impacts:

            signal = (
                impact["signal"]
                ["domain"]
            )

            if signal not in labels:

                labels.append(
                    signal
                )

            for downstream in impact.get(
                "downstream_impacts",
                []
            ):

                if downstream not in labels:

                    labels.append(
                        downstream
                    )

                sources.append(
                    labels.index(
                        signal
                    )
                )

                targets.append(
                    labels.index(
                        downstream
                    )
                )

        values = [
            1
        ] * len(
            sources
        )

        fig = go.Figure(

            go.Sankey(

                node=dict(
                    label=labels
                ),

                link=dict(

                    source=sources,

                    target=targets,

                    value=values
                )
            )
        )

        fig.update_layout(

            title=
                "Impact Propagation"
        )

        st.plotly_chart(

            fig,

            use_container_width=True
        )
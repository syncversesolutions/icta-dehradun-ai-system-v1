import streamlit as st


class RecommendationPanel:

    def __init__(self):
        pass

    def render(
        self,
        recommendations
    ):

        st.markdown(
            "### Recommendations"
        )

        for recommendation in recommendations:

            st.success(
                recommendation
            )
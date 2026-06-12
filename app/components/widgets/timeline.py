import streamlit as st


class Timeline:

    def __init__(self):
        pass

    def render(
        self,
        events
    ):

        st.markdown(
            "### Timeline"
        )

        for event in events:

            st.markdown(
                f"""
                • {event}
                """
            )
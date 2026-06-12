import streamlit as st


class EventFeed:

    def __init__(self):
        pass

    def render(
        self,
        memory
    ):

        st.subheader(
            "Recent Events"
        )

        if not memory:

            st.info(
                "No events available"
            )

            return

        for event in reversed(
            memory[-10:]
        ):

            st.markdown(

                f"""
                • {event.get('signal')}
                →
                {event.get('workflow')}
                →
                {event.get('outcome')}
                """
            )
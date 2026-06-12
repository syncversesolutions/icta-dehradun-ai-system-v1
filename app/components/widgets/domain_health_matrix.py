import streamlit as st


class DomainHealthMatrix:

    def __init__(self):
        pass

    def render(
        self,
        domain_states
    ):

        if not domain_states:

            st.info(
                "No domain health data available."
            )

            return

        for domain, data in (

            domain_states.items()

        ):

            status = data.get(
                "status",
                "unknown"
            )

            score = data.get(
                "score",
                0
            )

            message = data.get(
                "message",
                "No status available"
            )

            with st.container(
                border=True
            ):

                st.write(
                    f"### {domain.title()}"
                )

                st.write(
                    f"**Status:** {status.upper()}"
                )

                st.write(
                    f"**Score:** {score}"
                )

                st.write(
                    message
                )
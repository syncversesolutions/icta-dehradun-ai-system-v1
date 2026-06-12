import streamlit as st


class DomainRelationshipGraph:

    def __init__(self):
        pass

    def render(
        self,
        domains
    ):

        st.subheader(
            "Domain Relationships"
        )

        st.write(domains)
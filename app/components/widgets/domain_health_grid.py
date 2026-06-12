import streamlit as st

from components.cards.domain_card import (
    DomainCard
)


class DomainHealthGrid:

    def __init__(self):

        self.card = DomainCard()

    def render(
        self,
        domains
    ):

        cols = st.columns(
            len(domains)
        )

        for col, domain in zip(
            cols,
            domains
        ):

            with col:

                self.card.render(

                    domain["name"],

                    domain["status"]
                )
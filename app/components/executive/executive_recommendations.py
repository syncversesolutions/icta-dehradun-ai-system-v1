from components.cards.ai_card import (
    AICard
)


class ExecutiveRecommendations:

    def __init__(self):

        self.card = AICard()

    def render(
        self,
        recommendations
    ):

        for recommendation in recommendations:

            self.card.render(
                "AI Recommendation",
                recommendation
            )
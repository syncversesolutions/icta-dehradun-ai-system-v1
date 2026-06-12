from components.cards.action_card import (
    ActionCard
)

from components.workflows.autonomous_action_flow import (
    AutonomousActionFlow
)


class ExecutiveActions:

    def __init__(self):

        self.card = ActionCard()

        self.flow = (
            AutonomousActionFlow()
        )

    def render(
        self,
        actions
    ):

        self.flow.render(
            actions
        )

        for action in actions:

            self.card.render(
                action
            )
from components.cards.signal_card import (
    SignalCard
)

from components.charts.signal_chart import (
    SignalChart
)


class ExecutiveSignals:

    def __init__(self):

        self.card = SignalCard()

        self.chart = SignalChart()

    def render(
        self,
        signals
    ):

        self.chart.render(
            signals
        )

        for signal in signals[:5]:

            self.card.render(
                signal
            )
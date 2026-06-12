from components.cards.forecast_card import (
    ForecastCard
)

from components.charts.forecast_trend_chart import (
    ForecastTrendChart
)


class ExecutiveForecasts:

    def __init__(self):

        self.card = ForecastCard()

        self.chart = (
            ForecastTrendChart()
        )

    def render(
        self,
        forecasts
    ):

        self.chart.render(
            forecasts
        )

        for forecast in forecasts:

            self.card.render(
                forecast
            )
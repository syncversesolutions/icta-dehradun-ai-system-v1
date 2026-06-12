from components.widgets.metric_grid import (
    MetricGrid
)


class ExecutiveKPIs:

    def __init__(self):

        self.grid = MetricGrid()

    def render(
        self,
        state
    ):

        metrics = [

            {
                "title": "Risk Level",
                "value": state.get(
                    "risk_level",
                    "Unknown"
                )
            },

            {
                "title": "Signals",
                "value": len(
                    state.get(
                        "active_signals",
                        []
                    )
                )
            },

            {
                "title": "Forecasts",
                "value": state.get(
                    "forecast_count",
                    0
                )
            },

            {
                "title": "Actions",
                "value": state.get(
                    "autonomous_action_count",
                    0
                )
            }
        ]

        self.grid.render(
            metrics
        )
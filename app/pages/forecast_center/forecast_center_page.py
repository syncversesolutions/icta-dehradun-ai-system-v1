import streamlit as st

from components.widgets.executive_banner import (
    ExecutiveBanner
)

from components.charts.forecast_trend_chart import (
    ForecastTrendChart
)

from components.charts.risk_distribution_chart import (
    RiskDistributionChart
)

from components.tables.forecast_table import (
    ForecastTable
)

from pages.forecast_center.services.forecast_center_service import (
    ForecastCenterService
)


class ForecastCenterPage:

    def __init__(self):

        self.service = (
            ForecastCenterService()
        )

        self.banner = (
            ExecutiveBanner()
        )

        self.forecast_chart = (
            ForecastTrendChart()
        )

        self.risk_chart = (
            RiskDistributionChart()
        )

        self.table = (
            ForecastTable()
        )

    def render(self):

        data = (
            self.service.get_data()
        )

        forecasts = data.get(
            "forecasts",
            []
        )

        self.banner.render(

            title=
                "Forecast Center",

            subtitle=
                "Predictive Risk Intelligence"
        )

        st.markdown("---")

        self.forecast_chart.render(
            forecasts
        )

        st.markdown("---")

        self.table.render(
            forecasts
        )
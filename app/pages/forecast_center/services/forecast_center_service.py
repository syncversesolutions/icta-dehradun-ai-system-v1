import json

from pathlib import Path

from config.paths import BASE_DIR


class ForecastCenterService:

    def __init__(self):

        root = Path(BASE_DIR)

        self.forecast_file = (
            root /
            "system/prediction/forecasts/latest_forecast.json"
        )

    def get_data(self):

        if not self.forecast_file.exists():

            return {}

        with open(
            self.forecast_file
        ) as f:

            return json.load(f)
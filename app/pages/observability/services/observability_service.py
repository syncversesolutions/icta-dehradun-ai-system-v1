import json

from pathlib import Path

from config.paths import BASE_DIR


class ObservabilityService:

    def __init__(self):

        root = Path(BASE_DIR)

        self.state_file = (
            root /
            "system/state/global/global_state.json"
        )

    def get_data(self):

        if not self.state_file.exists():

            return {}

        with open(
            self.state_file,
            "r"
        ) as file:

            return json.load(
                file
            )
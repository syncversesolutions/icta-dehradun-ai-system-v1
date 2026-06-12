import json


class ScenarioLabService:

    def __init__(self):

        self.path = (
            "/content/drive/MyDrive/project_cd/"
            "system/prediction/scenarios/"
            "latest_scenarios.json"
        )

    def get_scenarios(self):

        with open(
            self.path
        ) as f:

            data = json.load(f)

        return data.get(
            "scenarios",
            []
        )
import json

from pathlib import Path

from config.paths import BASE_DIR


class IntelligenceCenterService:

    def __init__(self):

        root = Path(BASE_DIR)

        self.signal_file = (
            root /
            "system/signals/all_signals.json"
        )

        self.impact_file = (
            root /
            "system/graph/impact_analysis.json"
        )

        self.dependency_file = (
            root /
            "system/graph/dependency_graph.json"
        )

    def load_json(
        self,
        path,
        default
    ):

        if not path.exists():

            return default

        with open(
            path,
            "r"
        ) as f:

            return json.load(f)

    def get_data(self):

        return {

            "signals":
                self.load_json(
                    self.signal_file,
                    []
                ),

            "impacts":
                self.load_json(
                    self.impact_file,
                    []
                ),

            "dependencies":
                self.load_json(
                    self.dependency_file,
                    {}
                )
        }
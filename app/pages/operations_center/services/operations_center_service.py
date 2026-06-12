import json

from pathlib import Path

from config.paths import BASE_DIR


class OperationsCenterService:

    def __init__(self):

        root = Path(BASE_DIR)

        self.autonomy_file = (
            root /
            "system/autonomy/state/autonomy_state.json"
        )

        self.workflow_file = (
            root /
            "system/state/workflows/executions/workflow_executions.json"
        )

    def load_json(
        self,
        path,
        default
    ):

        if not path.exists():

            return default

        with open(path) as f:

            return json.load(f)

    def get_data(self):

        return {

            "autonomy":
                self.load_json(
                    self.autonomy_file,
                    {}
                ),

            "workflows":
                self.load_json(
                    self.workflow_file,
                    []
                )
        }
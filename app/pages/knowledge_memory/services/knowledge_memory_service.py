import json

from pathlib import Path

from config.paths import BASE_DIR


class KnowledgeMemoryService:

    def __init__(self):

        root = Path(BASE_DIR)

        self.memory_file = (
            root /
            "system/memory/history/episodic_memory.json"
        )

        self.learning_file = (
            root /
            "system/memory/learning/learning_history.json"
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

            "memory":
                self.load_json(
                    self.memory_file,
                    []
                ),

            "learning":
                self.load_json(
                    self.learning_file,
                    []
                )
        }
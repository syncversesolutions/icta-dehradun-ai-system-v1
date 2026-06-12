import json

from pathlib import Path

from config.paths import BASE_DIR


class RuntimeConfigLoader:

    def __init__(self):

        # ====================================
        # RUNTIME ROOT
        # ====================================

        self.runtime_root = (

            Path(BASE_DIR) /

            "config/runtime"
        )

    # ========================================
    # LOAD CONFIG
    # ========================================

    def load(

        self,
        category,
        filename

    ):

        config_path = (

            self.runtime_root /

            category /

            filename
        )

        with open(
            config_path,
            "r"
        ) as f:

            config = json.load(f)

        print(
            "\nRuntime config loaded ✅"
        )

        print(f"\nCategory: {category}")

        print(f"File: {filename}")

        return config

    # ========================================
    # DISPLAY CONFIG
    # ========================================

    def display(

        self,
        config

    ):

        print("\n")
        print("=" * 60)

        print("ICTA RUNTIME CONFIG")

        print("=" * 60)

        for key, value in config.items():

            print(f"\n{key}:")
            print(value)

        print("\n")
        print("=" * 60)
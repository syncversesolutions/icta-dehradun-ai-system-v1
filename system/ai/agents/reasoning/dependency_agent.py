import json

from pathlib import Path
from datetime import datetime

from config.paths import BASE_DIR


class DependencyAgent:

    def __init__(self):

        self.graph_path = (
            Path(BASE_DIR)
            / "system/graph/dependency_graph.json"
        )

        self.observation_path = (
            Path(BASE_DIR)
            / "system/state/agents/state_analyst_state.json"
        )

        self.agent_state_path = (
            Path(BASE_DIR)
            / "system/state/agents/dependency_agent_state.json"
        )

    # =====================================
    # LOAD JSON
    # =====================================

    def load_json(self, path):

        if not path.exists():

            return {}

        with open(path, "r") as f:

            return json.load(f)

    # =====================================
    # SAVE STATE
    # =====================================

    def save_agent_state(
        self,
        state
    ):

        self.agent_state_path.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        with open(
            self.agent_state_path,
            "w"
        ) as f:

            json.dump(
                state,
                f,
                indent=4
            )

    # =====================================
    # ANALYZE
    # =====================================

    def analyze(self):

        analyst_state = self.load_json(
            self.observation_path
        )

        graph = self.load_json(
            self.graph_path
        )

        critical_domains = analyst_state.get(
            "critical_domains",
            []
        )

        affected_domains = set()

        affected_signals = []

        for domain in critical_domains:

            for signal_name, signal_data in graph.items():

                if signal_name.startswith(
                    f"{domain}."
                ):

                    impacts = signal_data.get(
                        "affects",
                        []
                    )

                    for impact in impacts:

                        affected_signals.append(
                            impact
                        )

                        impacted_domain = (
                            impact.split(".")[0]
                        )

                        affected_domains.add(
                            impacted_domain
                        )

        result = {

            "agent":
                "dependency_agent",

            "status":
                "completed",

            "timestamp":
                str(datetime.now()),

            "source_domains":
                critical_domains,

            "affected_domains":
                sorted(
                    list(
                        affected_domains
                    )
                ),

            "affected_signals":
                sorted(
                    list(
                        set(
                            affected_signals
                        )
                    )
                ),

            "affected_count":
                len(
                    affected_domains
                )
        }

        self.save_agent_state(
            result
        )

        return result

    # =====================================
    # DISPLAY
    # =====================================

    def display(self):

        result = self.analyze()

        print("\n")
        print("=" * 60)
        print("DEPENDENCY AGENT")
        print("=" * 60)

        print(
            "\nSource Domains:"
        )

        for item in result[
            "source_domains"
        ]:

            print(
                f"• {item}"
            )

        print(
            "\nAffected Domains:"
        )

        for item in result[
            "affected_domains"
        ]:

            print(
                f"• {item}"
            )

        print(
            "\nAffected Signals:"
        )

        for item in result[
            "affected_signals"
        ]:

            print(
                f"• {item}"
            )

        print("\n")
        print("=" * 60)
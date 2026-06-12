import json

from pathlib import Path

from datetime import datetime

from config.paths import BASE_DIR


class StateManager:

    def __init__(self):

        self.state_path = (
            Path(BASE_DIR)
            / "system/state/system_state.json"
        )

        self.initialize_state()

    # ==================================================
    # DEFAULT STATE SCHEMA
    # ==================================================

    def get_default_state(self):

        return {

            "system_status": "active",

            "risk_level": "low",

            "active_alerts": [],

            "critical_domains": [],

            "active_workflows": [],

            "active_signals": [],

            "domain_states": {

                "traffic": {},

                "accommodation": {},

                "crowd": {},

                "weather": {},

                "health": {},

                "tourism": {},

                "governance": {}
            },

            "impact_analysis": [],

            "recommendations": [],

            "last_signal": None,

            "last_orchestration": None,

            "last_pipeline_run": None,

            "domains_active": [],

            "artifacts_generated": [],

            "event_history_count": 0,

            "updated_at": str(
                datetime.now()
            )
        }

    # ==================================================
    # INITIALIZE STATE
    # ==================================================

    def initialize_state(self):

        if not self.state_path.exists():

            self.state_path.parent.mkdir(
                parents=True,
                exist_ok=True
            )

            default_state = (
                self.get_default_state()
            )

            with open(
                self.state_path,
                "w"
            ) as f:

                json.dump(
                    default_state,
                    f,
                    indent=4
                )

            print(
                "\nSystem state initialized ✅"
            )

    # ==================================================
    # LOAD STATE
    # ==================================================

    def load_state(self):

        with open(
            self.state_path,
            "r"
        ) as f:

            state = json.load(f)

        required_keys = (
            self.get_default_state()
        )

        for key, default in required_keys.items():

            if key not in state:

                state[key] = default

        return state

    # ==================================================
    # SAVE STATE
    # ==================================================

    def save_state(self, state):

        state["updated_at"] = str(
            datetime.now()
        )

        with open(
            self.state_path,
            "w"
        ) as f:

            json.dump(
                state,
                f,
                indent=4
            )

    # ==================================================
    # GET GLOBAL STATE
    # ==================================================

    def get_global_state(self):

        return self.load_state()

    # ==================================================
    # UPDATE DOMAIN STATE
    # ==================================================

    def update_domain_state(

        self,
        domain,
        domain_state

    ):

        state = self.load_state()

        state["domain_states"][
            domain
        ] = domain_state

        if (
            domain
            not in state[
                "domains_active"
            ]
        ):

            state[
                "domains_active"
            ].append(domain)

        self.save_state(state)

        print(
            f"\n{domain} state updated ✅"
        )

        return state

    # ==================================================
    # REGISTER SIGNAL
    # ==================================================

    def register_signal(

        self,
        signal

    ):

        state = self.load_state()

        state[
            "active_signals"
        ].append(signal)

        state[
            "last_signal"
        ] = signal.get(
            "signal_id",
            "unknown"
        )

        self.save_state(state)

        print(
            "\nSignal registered ✅"
        )

        return state

    # ==================================================
    # UPDATE IMPACT ANALYSIS
    # ==================================================

    def update_impact_analysis(

        self,
        impacts

    ):

        state = self.load_state()

        state[
            "impact_analysis"
        ] = impacts

        self.save_state(state)

        print(
            "\nImpact analysis updated ✅"
        )

        return state

    # ==================================================
    # UPDATE RECOMMENDATIONS
    # ==================================================

    def update_recommendations(

        self,
        recommendations

    ):

        state = self.load_state()

        state[
            "recommendations"
        ] = recommendations

        self.save_state(state)

        print(
            "\nRecommendations updated ✅"
        )

        return state

    # ==================================================
    # UPDATE PIPELINE EXECUTION
    # ==================================================

    def update_pipeline_run(

        self,
        pipeline_name

    ):

        state = self.load_state()

        state[
            "last_pipeline_run"
        ] = str(
            datetime.now()
        )

        if (
            pipeline_name
            not in state[
                "active_workflows"
            ]
        ):

            state[
                "active_workflows"
            ].append(
                pipeline_name
            )

        self.save_state(state)

        return state

    # ==================================================
    # REGISTER GENERATED ARTIFACT
    # ==================================================

    def register_artifact(

        self,
        artifact_name

    ):

        state = self.load_state()

        if (
            artifact_name
            not in state[
                "artifacts_generated"
            ]
        ):

            state[
                "artifacts_generated"
            ].append(
                artifact_name
            )

        self.save_state(state)

        return state

    # ==================================================
    # UPDATE FROM ALERT
    # ==================================================

    def update_from_alert(

        self,
        alert

    ):

        state = self.load_state()

        state[
            "system_status"
        ] = (

            "critical"

            if alert[
                "severity"
            ] == "SEVERE"

            else "elevated"
        )

        state[
            "risk_level"
        ] = alert[
            "risk_level"
        ]

        state[
            "active_alerts"
        ].append({

            "source_signal":
                alert[
                    "source_signal"
                ],

            "severity":
                alert[
                    "severity"
                ],

            "timestamp":
                alert[
                    "timestamp"
                ]
        })

        state[
            "critical_domains"
        ] = alert[
            "affected_domains"
        ]

        state[
            "last_signal"
        ] = alert[
            "source_signal"
        ]

        state[
            "last_orchestration"
        ] = str(
            datetime.now()
        )

        state[
            "event_history_count"
        ] += 1

        self.save_state(state)

        return state

    # ==================================================
    # CLEAR SIGNALS
    # ==================================================

    def clear_signals(self):

        state = self.load_state()

        state[
            "active_signals"
        ] = []

        self.save_state(state)

    # ==================================================
    # CLEAR RECOMMENDATIONS
    # ==================================================

    def clear_recommendations(self):

        state = self.load_state()

        state[
            "recommendations"
        ] = []

        self.save_state(state)

    # ==================================================
    # DISPLAY STATE
    # ==================================================

    def display_state(self):

        state = self.load_state()

        print("\n")
        print("=" * 80)

        print(
            "ICTA GLOBAL SYSTEM STATE"
        )

        print("=" * 80)

        print(
            f"\nSystem Status : "
            f"{state['system_status']}"
        )

        print(
            f"\nRisk Level : "
            f"{state['risk_level']}"
        )

        print(
            f"\nDomains Active : "
            f"{state['domains_active']}"
        )

        print(
            f"\nCritical Domains : "
            f"{state['critical_domains']}"
        )

        print(
            f"\nActive Alerts : "
            f"{len(state['active_alerts'])}"
        )

        print(
            f"\nActive Signals : "
            f"{len(state['active_signals'])}"
        )

        print(
            f"\nRecommendations : "
            f"{len(state['recommendations'])}"
        )

        print(
            f"\nArtifacts Generated : "
            f"{len(state['artifacts_generated'])}"
        )

        print(
            f"\nEvent History Count : "
            f"{state['event_history_count']}"
        )

        print(
            f"\nLast Signal : "
            f"{state['last_signal']}"
        )

        print(
            f"\nLast Pipeline Run : "
            f"{state['last_pipeline_run']}"
        )

        print(
            f"\nUpdated At : "
            f"{state['updated_at']}"
        )

        print("\n")
        print("=" * 80)
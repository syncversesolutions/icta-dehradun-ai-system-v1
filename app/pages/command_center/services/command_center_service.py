import json

from pathlib import Path

from config.paths import BASE_DIR


class CommandCenterService:

    def __init__(self):

        root = Path(BASE_DIR)

        self.state_file = (
            root /
            "system/state/global/global_state.json"
        )

        self.signal_file = (
            root /
            "system/signals/all_signals.json"
        )

        self.impact_file = (
            root /
            "system/graph/impact_analysis.json"
        )

        self.alert_file = (
            root /
            "system/ai/active_alerts.json"
        )

        self.forecast_file = (
            root /
            "system/prediction/forecasts/latest_forecast.json"
        )

        self.scenario_file = (
            root /
            "system/prediction/scenarios/latest_scenarios.json"
        )

        self.autonomy_file = (
            root /
            "system/autonomy/state/autonomy_state.json"
        )

        self.memory_file = (
            root /
            "system/memory/history/episodic_memory.json"
        )

    # ==========================================
    # LOAD JSON
    # ==========================================

    def load_json(
        self,
        path,
        default
    ):

        if not path.exists():

            return default

        try:

            with open(
                path,
                "r"
            ) as file:

                return json.load(
                    file
                )

        except Exception:

            return default

    # ==========================================
    # EXECUTIVE SUMMARY
    # ==========================================

    def build_summary(
        self,
        data
    ):

        signals = data["signals"]

        forecasts = (
            data["forecasts"].get(
                "forecasts",
                []
            )
            if isinstance(
                data["forecasts"],
                dict
            )
            else []
        )

        scenarios = (
            data["scenarios"].get(
                "scenarios",
                []
            )
            if isinstance(
                data["scenarios"],
                dict
            )
            else []
        )

        memory = data["memory"]

        autonomy = data["autonomy"]

        critical_signals = [

            signal

            for signal in signals

            if signal.get(
                "risk_level",
                ""
            ).lower() == "high"
        ]

        critical_count = len(
            critical_signals
        )

        if critical_count > 15:

            risk_level = (
                "CRITICAL"
            )

        elif critical_count > 5:

            risk_level = (
                "HIGH"
            )

        elif critical_count > 0:

            risk_level = (
                "MEDIUM"
            )

        else:

            risk_level = (
                "LOW"
            )

        highest_signal = None

        if signals:

            highest_signal = max(

                signals,

                key=lambda x:
                x.get(
                    "predicted_score",
                    0
                )
            )

        return {

            "system_health":
                "ACTIVE",

            "risk_level":
                risk_level,

            "active_signals":
                len(
                    signals
                ),

            "critical_signals":
                critical_count,

            "forecast_count":
                len(
                    forecasts
                ),

            "scenario_count":
                len(
                    scenarios
                ),

            "autonomous_actions":
                len(

                    autonomy.get(
                        "execution_logs",
                        []
                    )
                ),

            "memory_episodes":
                len(
                    memory
                ),

            "highest_risk_location":

                highest_signal.get(
                    "checkpoint_name",
                    "Unknown"
                )

                if highest_signal
                else "Unknown",

            "highest_risk_score":

                round(

                    highest_signal.get(
                        "predicted_score",
                        0
                    ),

                    2

                )

                if highest_signal
                else 0,

            "highest_risk_route":

                highest_signal.get(
                    "route_id",
                    "Unknown"
                )

                if highest_signal
                else "Unknown"
        }
    # ==========================================
    # DOMAIN HEALTH
    # ==========================================

    def build_domain_health(
        self,
        data
    ):

        traffic_signals = [

            signal

            for signal in data["signals"]

            if signal.get(
                "domain"
            ) == "traffic"
        ]

        traffic_count = len(
            traffic_signals
        )

        if traffic_count > 15:

            traffic_status = (
                "critical"
            )

        elif traffic_count > 5:

            traffic_status = (
                "warning"
            )

        else:

            traffic_status = (
                "healthy"
            )

        traffic_score = max(

            0,

            100 - (
                traffic_count * 3
            )
        )

        return {

            "traffic": {

                "status":
                    traffic_status,

                "score":
                    traffic_score,

                "message":
                    (
                        f"{traffic_count} "
                        f"active congestion signals"
                    )
            },

            "accommodation": {

                "status":
                    "healthy",

                "score":
                    92,

                "message":
                    "Capacity Available"
            },

            "crowd": {

                "status":
                    "healthy",

                "score":
                    88,

                "message":
                    "Crowd Stable"
            },

            "weather": {

                "status":
                    "healthy",

                "score":
                    95,

                "message":
                    "No Active Alerts"
            },

            "health": {

                "status":
                    "healthy",

                "score":
                    90,

                "message":
                    "Medical Capacity Available"
            },

            "tourism": {

                "status":
                    "healthy",

                "score":
                    87,

                "message":
                    "Tourism Operations Stable"
            },

            "governance": {

                "status":
                    "healthy",

                "score":
                    91,

                "message":
                    "Decision Workflows Active"
            }
        }

    # ==========================================
    # RISK PROFILE
    # ==========================================

    def build_risk_profile(
        self,
        data
    ):

        signals = data["signals"]

        high = 0
        medium = 0
        low = 0

        for signal in signals:

            level = signal.get(
                "risk_level",
                ""
            ).lower()

            if level == "high":

                high += 1

            elif level == "medium":

                medium += 1

            else:

                low += 1

        return {

            "high":
                high,

            "medium":
                medium,

            "low":
                low
        }

    # ==========================================
    # RECENT EVENTS
    # ==========================================

    def build_recent_events(
        self,
        data
    ):

        memory = data["memory"]

        events = []

        for item in memory[-20:]:

            events.append({

                "signal":
                    item.get(
                        "signal",
                        "unknown"
                    ),

                "workflow":
                    item.get(
                        "workflow",
                        "unknown"
                    ),

                "outcome":
                    item.get(
                        "outcome",
                        "unknown"
                    )
            })

        return events

    # ==========================================
    # LOAD RAW DATA
    # ==========================================

    def load_raw_data(
        self
    ):

        return {

            "state":
                self.load_json(
                    self.state_file,
                    {}
                ),

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

            "alerts":
                self.load_json(
                    self.alert_file,
                    []
                ),

            "forecasts":
                self.load_json(
                    self.forecast_file,
                    {}
                ),

            "scenarios":
                self.load_json(
                    self.scenario_file,
                    {}
                ),

            "autonomy":
                self.load_json(
                    self.autonomy_file,
                    {}
                ),

            "memory":
                self.load_json(
                    self.memory_file,
                    []
                )
        }

    # ==========================================
    # MAIN AGGREGATOR
    # ==========================================

    def get_data(
        self
    ):

        data = (
            self.load_raw_data()
        )

        data["summary"] = (
            self.build_summary(
                data
            )
        )

        data["domain_health"] = (
            self.build_domain_health(
                data
            )
        )

        data["risk_profile"] = (
            self.build_risk_profile(
                data
            )
        )

        data["recent_events"] = (
            self.build_recent_events(
                data
            )
        )

        return data
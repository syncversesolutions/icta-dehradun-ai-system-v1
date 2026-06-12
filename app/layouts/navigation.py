class Navigation:

    def get_route(

        self,
        page

    ):

        routes = {

            # ====================================
            # EXECUTIVE LAYER
            # ====================================

            "Command Center":
                "command_center",

            "Intelligence Center":
                "intelligence_center",

            "Forecast Center":
                "forecast_center",

            "Scenario Lab":
                "scenario_lab",

            "Operations Center":
                "operations_center",

            "Knowledge & Memory":
                "knowledge_memory",

            # ====================================
            # DOMAIN LAYER
            # ====================================

            "Traffic":
                "traffic",

            "Crowd":
                "crowd",

            "Accommodation":
                "accommodation",

            # ====================================
            # PLATFORM LAYER
            # ====================================

            "Observability":
                "observability"
        }

        return routes.get(page)
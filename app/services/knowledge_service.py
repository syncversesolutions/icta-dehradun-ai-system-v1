class KnowledgeService:
    def __init__(self):
        pass
    # ========================================
    # GET REASONING
    # ========================================
    def get_reasoning(self):
        return [
            {
                "signal":
                    "occupancy_rate",
                "inference":
                    "Traffic pressure likely"
            },
            {
                "signal":
                    "crowd_density",
                "inference":
                    "Medical escalation possible"
            }
        ]
    # ========================================
    # GET RELATIONSHIPS
    # ========================================
    def get_relationships(self):
        return [
            {
                "source":
                    "Accommodation",
                "target":
                    "Traffic"
            },
            {
                "source":
                    "Traffic",
                "target":
                    "Crowd"
            },
            {
                "source":
                    "Crowd",
                "target":
                    "Medical"
            },
            {
                "source":
                    "Medical",
                "target":
                    "Emergency"
            },
            {
                "source":
                    "Weather",
                "target":
                    "Traffic"
            },
            {
                "source":
                    "Traffic",
                "target":
                    "Accommodation"
            }
        ]
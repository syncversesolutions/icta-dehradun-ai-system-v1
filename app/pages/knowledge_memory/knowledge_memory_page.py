import streamlit as st

from components.widgets.executive_banner import (
    ExecutiveBanner
)

from components.widgets.timeline import (
    Timeline
)

from components.telemetry.memory_activity import (
    MemoryActivity
)

from pages.knowledge_memory.services.knowledge_memory_service import (
    KnowledgeMemoryService
)


class KnowledgeMemoryPage:

    def __init__(self):

        self.service = (
            KnowledgeMemoryService()
        )

        self.banner = (
            ExecutiveBanner()
        )

        self.memory_activity = (
            MemoryActivity()
        )

        self.timeline = (
            Timeline()
        )

    def render(self):

        data = (
            self.service.get_data()
        )

        memory = data["memory"]

        self.banner.render(

            title=
                "Knowledge & Memory",

            subtitle=
                "Learning Intelligence & Memory Evolution"
        )

        st.markdown("---")

        self.memory_activity.render(
            memory
        )

        st.markdown("---")

        events = []

        for episode in memory[-20:]:

            events.append(

                f"{episode.get('signal')} → "
                f"{episode.get('workflow')} → "
                f"{episode.get('outcome')}"
            )

        self.timeline.render(
            events
        )
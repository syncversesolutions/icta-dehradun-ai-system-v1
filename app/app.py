from streamlit_autorefresh import (
    st_autorefresh
)

# ============================================
# RUNTIME ENVIRONMENT
# ============================================

import runpy

runpy.run_path(
    "/content/drive/MyDrive/project_cd/"
    "config/runtime_environment.py"
)

# ============================================
# IMPORTS
# ============================================

import streamlit as st
from pathlib import Path

# ============================================
# LAYOUTS
# ============================================

from layouts.sidebar import (
    Sidebar
)

from layouts.navigation import (
    Navigation
)

# ============================================
# THEMES
# ============================================


from themes.dark_theme import (
    DarkTheme
)

from themes.light_theme import (
    LightTheme
)

# ============================================
# EXECUTIVE LAYER
# ============================================

from pages.command_center.command_center_page import (
    CommandCenterPage
)

from pages.intelligence_center.intelligence_center_page import (
    IntelligenceCenterPage
)

from pages.forecast_center.forecast_center_page import (
    ForecastCenterPage
)

from pages.scenario_lab.scenario_lab_page import (
    ScenarioLabPage
)

from pages.operations_center.operations_center_page import (
    OperationsCenterPage
)

from pages.knowledge_memory.knowledge_memory_page import (
    KnowledgeMemoryPage
)

# ============================================
# DOMAIN LAYER
# ============================================

from pages.traffic.traffic_page import (
    TrafficPage
)

from pages.crowd.crowd_page import (
    CrowdPage
)

from pages.accommodation.accommodation_page import (
    AccommodationPage
)

# ============================================
# PLATFORM LAYER
# ============================================

from pages.observability.observability_page import (
    ObservabilityPage
)

# ============================================
# PAGE CONFIG
# ============================================

st.set_page_config(

    page_title=
        "ICTA Command Center",

    page_icon=
        "🧠",

    layout=
        "wide",

    initial_sidebar_state=
        "expanded"
)

from styles.theme_loader import ThemeLoader
ThemeLoader.load()

# ============================================
# AUTO REFRESH
# ============================================

st_autorefresh(

    interval=30000,

    key="icta_refresh"
)

# ============================================
# SIDEBAR
# ============================================

sidebar = Sidebar()

sidebar_state = (
    sidebar.render()
)

selected_page = (
    sidebar_state["page"]
)

selected_theme = (
    sidebar_state["theme"]
)

# ============================================
# APPLY THEME
# ============================================

if selected_theme == "Dark":

    theme = DarkTheme()

else:

    theme = LightTheme()

theme.apply()

# ============================================
# ROUTING
# ============================================

navigation = Navigation()

route = navigation.get_route(
    selected_page
)

# ============================================
# COMMAND CENTER
# ============================================

if route == "command_center":

    page = CommandCenterPage()

    page.render()

# ============================================
# INTELLIGENCE CENTER
# ============================================

elif route == "intelligence_center":

    page = IntelligenceCenterPage()

    page.render()

# ============================================
# FORECAST CENTER
# ============================================

elif route == "forecast_center":

    page = ForecastCenterPage()

    page.render()

# ============================================
# SCENARIO LAB
# ============================================

elif route == "scenario_lab":

    page = ScenarioLabPage()

    page.render()

# ============================================
# OPERATIONS CENTER
# ============================================

elif route == "operations_center":

    page = OperationsCenterPage()

    page.render()

# ============================================
# KNOWLEDGE & MEMORY
# ============================================

elif route == "knowledge_memory":

    page = KnowledgeMemoryPage()

    page.render()

# ============================================
# TRAFFIC DOMAIN
# ============================================

elif route == "traffic":

    page = TrafficPage()

    page.render()

# ============================================
# CROWD DOMAIN
# ============================================

elif route == "crowd":

    page = CrowdPage()

    page.render()

# ============================================
# ACCOMMODATION DOMAIN
# ============================================

elif route == "accommodation":

    page = AccommodationPage()

    page.render()

# ============================================
# OBSERVABILITY
# ============================================

elif route == "observability":

    page = ObservabilityPage()

    page.render()

# ============================================
# FALLBACK
# ============================================

else:

    st.error(
        "Unknown page route"
    )
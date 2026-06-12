import streamlit as st


class Sidebar:

    def render(self):

        st.sidebar.title(
            "ICTA Platform"
        )

        theme = st.sidebar.selectbox(

            "Theme",

            [

                "Dark",
                "Light"
            ]
        )

        st.sidebar.markdown("---")

        st.sidebar.subheader(
            "Executive Layer"
        )

        page = st.sidebar.radio(

            "Navigation",

            [

                "Command Center",

                "Intelligence Center",

                "Forecast Center",

                "Scenario Lab",

                "Operations Center",

                "Knowledge & Memory",

                "Traffic",

                "Crowd",

                "Accommodation",

                "Observability"
            ]
        )

        return {

            "page":
                page,

            "theme":
                theme
        }
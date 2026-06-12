import streamlit as st


class ExecutiveBanner:

    def render(
        self,
        title,
        subtitle
    ):
        html = f"""
          <div class="icta-card">
            <h1>{title}</h1>
            <p>{subtitle}</p>
          </div>
          """   

        st.markdown(
            html,
            unsafe_allow_html=True
        )
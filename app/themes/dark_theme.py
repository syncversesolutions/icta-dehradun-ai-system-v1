import streamlit as st


class DarkTheme:

    def apply(self):

        st.markdown(
            """
            <style>

            /* ==================================================
               MAIN APPLICATION
            ================================================== */

            .stApp {
                background-color: #151A23;
                color: #F8FAFC;
            }

            .block-container {
                padding-top: 1.5rem;
                padding-left: 2rem;
                padding-right: 2rem;
                max-width: 100%;
            }

            /* ==================================================
               SIDEBAR
            ================================================== */

            section[data-testid="stSidebar"] {
                background-color: #10151E;
                border-right: 1px solid #334155;
            }

            section[data-testid="stSidebar"] * {
                color: #E2E8F0;
            }

            /* ==================================================
               HEADINGS
            ================================================== */

            h1 {
                color: #F8FAFC;
                font-size: 42px;
                font-weight: 700;
                letter-spacing: -0.5px;
            }

            h2 {
                color: #F8FAFC;
                font-size: 30px;
                font-weight: 600;
            }

            h3 {
                color: #E2E8F0;
                font-size: 22px;
                font-weight: 600;
            }

            h4 {
                color: #CBD5E1;
                font-size: 18px;
                font-weight: 500;
            }

            p {
                color: #94A3B8;
                font-size: 14px;
            }

            label {
                color: #CBD5E1;
            }

            /* ==================================================
               METRICS
            ================================================== */

            div[data-testid="metric-container"] {

                background-color: #1F2937;

                border: 1px solid #475569;

                border-radius: 16px;

                padding: 18px;

                box-shadow:
                0 0 0 1px rgba(255,255,255,0.03);

            }

            div[data-testid="metric-container"] label {
                color: #94A3B8;
            }

            div[data-testid="metric-container"] div {
                color: #F8FAFC;
            }

            /* ==================================================
               BUTTONS
            ================================================== */

            .stButton > button {

                background-color: #2563EB;

                color: white;

                border: none;

                border-radius: 10px;

                padding: 0.6rem 1.2rem;

                font-weight: 600;
            }

            .stButton > button:hover {

                background-color: #3B82F6;

                color: white;
            }

            /* ==================================================
               DATAFRAME
            ================================================== */

            .stDataFrame {

                border: 1px solid #334155;

                border-radius: 12px;

                overflow: hidden;
            }

            /* ==================================================
               EXPANDERS
            ================================================== */

            .streamlit-expanderHeader {

                background-color: #1F2937;

                border-radius: 10px;

                color: #E2E8F0;
            }

            /* ==================================================
               TABS
            ================================================== */

            button[data-baseweb="tab"] {

                background-color: #1F2937;

                color: #CBD5E1;

                border-radius: 10px;

                margin-right: 6px;

                padding: 10px 18px;
            }

            button[data-baseweb="tab"][aria-selected="true"] {

                background-color: #2563EB;

                color: white;
            }

            /* ==================================================
               SELECTBOX
            ================================================== */

            div[data-baseweb="select"] {

                background-color: #1F2937;

                border-radius: 10px;
            }

            /* ==================================================
               INPUTS
            ================================================== */

            .stTextInput input,
            .stNumberInput input,
            .stTextArea textarea {

                background-color: #1F2937;

                color: #F8FAFC;

                border: 1px solid #334155;

                border-radius: 10px;
            }

            /* ==================================================
               CARDS
            ================================================== */

            .icta-card {

                background-color: #1F2937;

                border: 1px solid #334155;

                border-radius: 18px;

                padding: 24px;

                margin-bottom: 20px;

                box-shadow:
                0px 2px 12px rgba(0,0,0,0.25);
            }

            .icta-card-title {

                color: #E2E8F0;

                font-size: 18px;

                font-weight: 600;

                margin-bottom: 10px;
            }

            .icta-card-value {

                color: #F8FAFC;

                font-size: 34px;

                font-weight: 700;
            }

            /* ==================================================
               ALERT CARDS
            ================================================== */

            .icta-alert {

                background-color: #2B1D1D;

                border-left: 5px solid #EF4444;

                border-radius: 12px;

                padding: 18px;

                margin-bottom: 12px;
            }

            /* ==================================================
               SUCCESS CARDS
            ================================================== */

            .icta-success {

                background-color: #132A1D;

                border-left: 5px solid #22C55E;

                border-radius: 12px;

                padding: 18px;

                margin-bottom: 12px;
            }

            /* ==================================================
               SCROLLBAR
            ================================================== */

            ::-webkit-scrollbar {
                width: 10px;
            }

            ::-webkit-scrollbar-track {
                background: #10151E;
            }

            ::-webkit-scrollbar-thumb {
                background: #334155;
                border-radius: 10px;
            }

            ::-webkit-scrollbar-thumb:hover {
                background: #475569;
            }

            /* ==================================================
               HORIZONTAL RULE
            ================================================== */

            hr {
                border: none;
                border-top: 1px solid #334155;
            }

            </style>
            """,
            unsafe_allow_html=True
        )
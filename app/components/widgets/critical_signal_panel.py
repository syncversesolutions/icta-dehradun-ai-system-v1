import streamlit as st


class CriticalSignalPanel:

    def __init__(self):
        pass

    def render(
        self,
        signals
    ):

        if not signals:

            st.info(
                "No active signals."
            )

            return

        signals = sorted(

            signals,

            key=lambda x:
            x.get(
                "predicted_score",
                0
            ),

            reverse=True
        )

        for signal in signals[:10]:

            with st.container(
                border=True
            ):

                col1, col2 = st.columns(
                    [3, 1]
                )

                with col1:

                    st.subheader(

                        signal.get(
                            "checkpoint_name",
                            "Unknown Checkpoint"
                        )
                    )

                    st.write(

                        f"**Signal Type:** "
                        f"{signal.get('signal_type','Unknown')}"
                    )

                    st.write(

                        f"**Route:** "
                        f"{signal.get('route_id','Unknown')}"
                    )

                    st.write(

                        f"**Domain:** "
                        f"{signal.get('domain','Unknown')}"
                    )

                with col2:

                    st.metric(

                        "Risk",

                        signal.get(
                            "risk_level",
                            "Unknown"
                        )
                    )

                    st.metric(

                        "Score",

                        round(

                            signal.get(
                                "predicted_score",
                                0
                            ),

                            2
                        )
                    )

                st.write(

                    f"**Recommended Action:** "
                    f"{signal.get('recommended_action','None')}"
                )
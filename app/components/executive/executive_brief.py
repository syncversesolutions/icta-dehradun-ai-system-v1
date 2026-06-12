import streamlit as st


class ExecutiveBrief:

    def __init__(self):
        pass

    def render(
        self,
        summary,
        signals
    ):

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

        st.write(

            f"**System Health:** "
            f"{summary.get('system_health','Unknown')}"
        )

        st.write(

            f"**Risk Level:** "
            f"{summary.get('risk_level','Unknown')}"
        )

        st.write(

            f"**Active Signals:** "
            f"{summary.get('active_signals',0)}"
        )

        if highest_signal:

            st.write(

                f"**Highest Risk Location:** "
                f"{highest_signal.get('checkpoint_name','Unknown')}"
            )

            st.write(

                f"**Primary Threat:** "
                f"{highest_signal.get('signal_type','Unknown')}"
            )

            st.write(

                f"**Recommended Response:** "
                f"{highest_signal.get('recommended_action','None')}"
            )
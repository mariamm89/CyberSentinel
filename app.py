
import pandas as pd
import streamlit as st
from detector import detect_brute_force

st.set_page_config(
    page_title="CyberSentinel",
    page_icon="🛡️",
    layout="wide"
)

st.title("🛡️ CyberSentinel")
st.subheader("Tableau de bord de détection des menaces")

st.write(
    "Analyse des journaux de connexion et détection "
    "des tentatives de force brute."
)

try:
    logs = pd.read_csv("logs.csv")
    alerts = detect_brute_force(logs)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Événements analysés", len(logs))

    with col2:
        st.metric("Alertes détectées", len(alerts))

    with col3:
        high_alerts = (
            len(alerts[alerts["severity"] == "HIGH"])
            if not alerts.empty else 0
        )
        st.metric("Alertes critiques (HIGH)", high_alerts)

    st.header("Résultats de l'analyse")

    if alerts.empty:
        st.success("Aucune alerte détectée.")
    else:
        st.warning("Des comportements suspects ont été détectés.")
        st.dataframe(alerts, use_container_width=True)

        csv_data = alerts.to_csv(index=False).encode("utf-8")

        st.download_button(
            label="Télécharger les alertes CSV",
            data=csv_data,
            file_name="alerts.csv",
            mime="text/csv"
        )

    with st.expander("Consulter les journaux analysés"):
        st.dataframe(logs, use_container_width=True)

except FileNotFoundError:
    st.error(
        "Fichier logs.csv introuvable. "
        "Exécute d'abord python generate_logs.py."
    )

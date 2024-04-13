import streamlit as st
import matplotlib.pyplot as plt
import random
import seaborn as sns

def time_graphs(df):
    graph_data = df[['end_date', 'Zas', 'Polluant', 'valeur']]
    pollutant_option = st.selectbox('Select Pollutant:', graph_data['Polluant'].unique())
    filtered_data = graph_data[graph_data['Polluant'] == pollutant_option]
    st.bar_chart(
        x='end_date',
        y='valeur',
        data=filtered_data,
    )

def measurements_by_pollutants(df):
    graph_data = df[['end_date', 'Polluant', 'valeur']]
    pollutant_option = st.selectbox('Select:', graph_data['Polluant'].unique())
    filtered_data = graph_data[graph_data['Polluant'] == pollutant_option]
    st.line_chart(
        x='end_date',
        y='valeur',
        data=filtered_data,
    )

    if filtered_data.empty:
        st.warning(f"No data found for pollutant: {pollutant_option}")

    st.download_button(
        label=f"Download Data for {pollutant_option}",
        data=filtered_data.to_csv(index=False),
        file_name=f"{pollutant_option}_data.csv",
        mime="text/csv",
    )

def alerts_and_regulatory_thresholds():
    labels = ["Date de début", "Date de fin", "Organisme", "code zas", "Zas", "code site", "nom site", "type d'implantation", "Polluant", "type d'influence", "discriminant", "Réglementaire", "type d'évaluation", "procédure de mesure", "type de valeur", "valeur", "valeur brute", "unité de mesure", "taux de saisie", "couverture temporelle", "couverture de données", "code qualité", "validité"]
    values = [10, 20, 15, 25, 30, 5, 12, 18, 22, 17, 8, 28, 19, 14, 11, 16, 23, 27, 21, 9, 13, 24, 26]
    regulatory_threshold = 20
    plt.figure(figsize=(14, 8))
    bars = plt.bar(labels, values, color='skyblue')
    for i in range(len(labels)):
        if values[i] > regulatory_threshold:
            plt.text(i, values[i] + 1, f'Alert: {values[i]}', ha='center')
    plt.axhline(y=regulatory_threshold, color='red', linestyle='--', linewidth=2)
    plt.xlabel('Labels')
    plt.ylabel('Values')
    plt.title('Alerts and Regulatory Thresholds')
    plt.xticks(rotation=90)
    st.pyplot(plt)


def pollution_sources_analysis(df):
    sources = df["type d'implantation"].unique()
    pollution_levels = df["code zas"]
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.stem(sources, pollution_levels)
    ax.set_xlabel('Pollution Sources')
    ax.set_ylabel('Pollution Levels')
    ax.set_title('Analysis of Pollution Sources')
    st.pyplot(fig)

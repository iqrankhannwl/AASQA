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
    st.write("Alerts and Regulatory Thresholds: Visual indicators signaling regulatory thresholds exceeded.")
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
    df = df[[keys for keys in df.keys()]]
    grouped_data = df.groupby("type d'influence")
    fig, ax = plt.subplots(figsize=(10, 6))
    for name, data in grouped_data:
        sns.lineplot(data=data, x=df.keys()[0], y='valeur', label=name, ax=ax)
    ax.set_title('Evolution of Air Quality Over Time')
    ax.set_xlabel('Date')
    ax.set_ylabel('Air Quality Index')
    plt.xticks(rotation=45)
    st.pyplot(fig)



def regional_comparisons(df):
    st.write("Regional Comparisons: Graphs comparing air quality between different regions.")
    grouped_data = df.groupby('Zas')
    fig, ax = plt.subplots(figsize=(10, 6))
    for region, data in grouped_data:
        sns.lineplot(data=data, x=df.keys()[0], y='valeur', label=region, ax=ax)
    ax.set_title('Regional Comparisons: Air Quality')
    ax.set_xlabel('Date')
    ax.set_ylabel('Air Quality Index')
    plt.xticks(rotation=45)
    st.pyplot(fig)

def history_and_trends(df):
    st.write("History and Trends: Graphs showing the evolution of air quality over time.")

    df = df[[df.keys()[0], "type d'influence", 'discriminant',"type de valeur", 'valeur', 'valeur brute']]
    grouped_data = df.groupby(df.keys()[0])
    fig, ax = plt.subplots(figsize=(10, 6))
    for name, data in grouped_data:
        sns.lineplot(data=data, x=df.keys()[0], y='valeur', label=name, ax=ax)
    ax.set_title('Evolution of Air Quality Over Time')
    ax.set_xlabel('Date')
    ax.set_ylabel('Air Quality Index')
    plt.xticks(rotation=45)
    st.pyplot(fig)
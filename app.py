import seaborn as sns
import streamlit as st
import pandas as pd
from scripts.data_processing import perform_data_analysis
import  matplotlib.pyplot as plt
from scripts.graphs import time_graphs,measurements_by_pollutants,alerts_and_regulatory_thresholds, pollution_sources_analysis
import warnings
warnings.filterwarnings('ignore')

st.set_page_config(page_title="Analytics Dashboard!!!", page_icon=":bar_chart:",layout="wide")

st.title(" :bar_chart: Sample Analytics Dashboard")
st.markdown("""
            <style>
            div.block-container{background-color: #96c6ea}
    .st-emotion-cache-6qob1r eczjsme3{
        background-color: #ddd;
    }
            </style>""",unsafe_allow_html=True)
st.sidebar.header("Analytics Dashboard!!!")


fl = st.file_uploader(":file_folder: Upload a file",type=(["csv","txt","xlsx","xls"]))
if fl is not None:
    df = pd.read_csv(fl, encoding = "ISO-8859-1", sep=";")
    df = df.rename(columns={'Date de fin': 'end_date'})

else:
    df = pd.read_csv("./data/upload/sample.csv", encoding = "ISO-8859-1", sep=";")
    df = df.rename(columns={'Date de fin': 'end_date'})


# Date de début;Date de fin;Organisme;code zas; Zas;code site;nom site;type d'implantation;Polluant;type d'influence;discriminant;Réglementaire;type d'évaluation;procédure de mesure;type de valeur;valeur;valeur brute;unité de mesure;taux de saisie;couverture temporelle;couverture de données;code qualité;validité

col1, col2 = st.columns((2))
with col1:
    time_graphs(df)
with col2:
    measurements_by_pollutants(df)

alerts_and_regulatory_thresholds()

col3,col4,col5=st.columns((3)) 
with col3:
    pollutant_counts = df['Polluant'].value_counts()
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.pie(pollutant_counts, labels=pollutant_counts.index, autopct='%1.1f%%', startangle=140)
    ax.set_title('Distribution of Organisme')
    st.pyplot(fig)
with col4:
    pollutant_counts = df[df.keys()[-2]].value_counts()
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.pie(pollutant_counts, labels=pollutant_counts.index, autopct='%1.1f%%', startangle=140)
    ax.set_title(f'Distribution of {df.keys()[-2]}')
    st.pyplot(fig)
    
with col5:
    pollutant_counts = df[df.keys()[5]].value_counts()
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.pie(pollutant_counts, labels=pollutant_counts.index, autopct='%1.1f%%', startangle=140)
    ax.set_title(f'Distribution of ')
    st.pyplot(fig)
# Display the plot using st.pyplot()


selected_column = st.selectbox('Select a categorical column:', df.columns)
colors = ['blue', 'green', 'red', 'purple', 'orange']
fig, ax = plt.subplots(figsize=(10, 6))
df[selected_column].value_counts().plot(kind='bar', ax=ax, color=colors)
plt.title(f'Count Plot of {selected_column}')
plt.xlabel('Count')
plt.ylabel(selected_column)
st.pyplot(fig)
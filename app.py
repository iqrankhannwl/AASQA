import seaborn as sns
import streamlit as st
import pandas as pd
from scripts.data_processing import perform_data_analysis
import  matplotlib.pyplot as plt
from scripts.graphs import time_graphs,measurements_by_pollutants,alerts_and_regulatory_thresholds, pollution_sources_analysis,regional_comparisons, history_and_trends
from src.Home import home_page
import warnings
warnings.filterwarnings('ignore')


def interactive_mapping():
    st.write("Interactive Mapping: Map display of measurement locations with colored markers indicating the levels of different pollutants.")

def meteorological_data():
    st.write("Meteorological Data: Integration of meteorological data to contextualize variations in air quality.")

def main():
    st.title("Air Quality Dashboard")
    fl = st.file_uploader(":file_folder: Upload a file",type=(["csv","txt","xlsx","xls"]))
    if fl is not None:
        df = pd.read_csv(fl, encoding = "ISO-8859-1", sep=";")
        df = df.rename(columns={'Date de fin': 'end_date'})

    else:
        df = pd.read_csv("./data/upload/sample.csv", encoding = "ISO-8859-1", sep=";")
        df = df.rename(columns={'Date de fin': 'end_date'})
    st.sidebar.title("Menu")
    menu_option = st.sidebar.radio("Go to", [
        "Home",
        "Time Graphs", 
        "Measurements by Pollutants", 
        "Alerts and Regulatory Thresholds", 
        "Pollution Sources", 
        "Regional Comparisons", 
        "History and Trends", 
        "Interactive Mapping", 
        "Meteorological Data"
    ])
    if menu_option == "Home":
        col12,col13=st.columns((2))
        with col12:
            fig, ax = plt.subplots(figsize=(8, 4))
            df['valeur'].plot(kind='line', ax=ax)
            ax.set_title('valeur')
            ax.spines[['top', 'right']].set_visible(False)
            st.pyplot(fig)

        with col13:
            fig, ax = plt.subplots(figsize=(8, 4))
            df['valeur brute'].plot(kind='line', ax=ax)
            ax.set_title('valeur')
            ax.spines[['top', 'right']].set_visible(False)
            st.pyplot(fig)
        df_2dhist = pd.DataFrame({
        x_label: grp[df.keys()[1]].value_counts()
        for x_label, grp in df.groupby(df.keys()[0])
        })
        fig, ax = plt.subplots(figsize=(8, 8))
        sns.heatmap(df_2dhist, cmap='viridis', ax=ax)
        ax.set_xlabel('Date de début')
        ax.set_ylabel('Date de fin')
        st.pyplot(fig)
        col15,col16=st.columns((2)) 
        with col15: 
            figsize = (12, 1.2 * len(df[df.keys()[0]].unique()))
            fig, ax = plt.subplots(figsize=figsize)
            sns.violinplot(data=df, x='valeur', y=df.keys()[0], inner='stick', palette='Dark2', ax=ax)
            sns.despine(top=True, right=True, bottom=True, left=True)
            st.pyplot(fig)
        with col16: 
            figsize = (12, 1.2 * len(df[df.keys()[1]].unique()))
            fig, ax = plt.subplots(figsize=figsize)
            sns.violinplot(data=df, x='valeur', y=df.keys()[1], inner='stick', palette='Dark2', ax=ax)
            sns.despine(top=True, right=True, bottom=True, left=True)
            st.pyplot(fig)
        home_page(df)


    if menu_option == "Time Graphs":
        time_graphs(df)
    elif menu_option == "Measurements by Pollutants":
        measurements_by_pollutants(df)
    elif menu_option == "Alerts and Regulatory Thresholds":
        alerts_and_regulatory_thresholds()
    elif menu_option == "Pollution Sources":
        pollution_sources_analysis(df)
    elif menu_option == "Regional Comparisons":
        regional_comparisons(df)
    elif menu_option == "History and Trends":
        history_and_trends(df)
    elif menu_option == "Interactive Mapping":
        interactive_mapping()
    elif menu_option == "Meteorological Data":
        meteorological_data()

if __name__ == "__main__":
    main()

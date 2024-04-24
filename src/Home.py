import seaborn as sns
import streamlit as st
import pandas as pd
import  matplotlib.pyplot as plt

import warnings
warnings.filterwarnings('ignore')

def _plot_series(series, series_name, series_index=0, target="valeur"):
    palette = list(sns.color_palette("Dark2"))
    xs = series[series.keys()[0]]
    ys = series[target]
    plt.plot(xs, ys, label=series_name, color=palette[series_index % len(palette)])

def home_page(df):
    col3,col4=st.columns((2))
    with col3:
        fig, ax = plt.subplots(figsize=(8, 6))
        df['valeur'].plot(kind='hist', bins=20, ax=ax)
        ax.set_title('Histogram of valeur')
        ax.spines[['top', 'right']].set_visible(False)
        st.pyplot(fig)

    with col4:
        fig, ax = plt.subplots(figsize=(8, 6))
        df['valeur brute'].plot(kind='hist', bins=20, ax=ax)
        ax.set_title('Histogram of valeur brute')
        ax.spines[['top', 'right']].set_visible(False)
        st.pyplot(fig)

    col5,col6=st.columns((2))
    with col5:
        fig, ax = plt.subplots(figsize=(8, 6))
        sns.countplot(y=df[df.keys()[0]], palette=sns.color_palette("Dark2"), ax=ax)
        ax.set_title('Bar Plot of Date de début')
        ax.spines[['top', 'right']].set_visible(False)
        st.pyplot(fig)
    with col6:
        fig, ax = plt.subplots(figsize=(8, 6))
        df.groupby(df.keys()[1]).size().plot(kind='barh', color=sns.color_palette("Dark2"), ax=ax)
        ax.set_title('Bar Plot of Date de fin')
        ax.spines[['top', 'right']].set_visible(False)
        st.pyplot(fig)

    col8,col9=st.columns((2))

    with col8:
            fig, ax = plt.subplots(figsize=(8, 6))
            df.plot(kind='scatter', x='valeur', y='valeur brute', s=32, alpha=.8, ax=ax)
            ax.set_xlabel('valeur')
            ax.set_ylabel('valeur brute')
            ax.spines[['top', 'right']].set_visible(False)
            st.pyplot(fig)
    with col9:
            df_sorted = df.sort_values(df.keys()[0], ascending=True)
            fig, ax = plt.subplots(figsize=(10, 5.2))
            for i, (series_name, series) in enumerate(df_sorted.groupby(df.keys()[0])):
                _plot_series(series, series_name, i, target="valeur")
            plt.legend(title='Date de début', bbox_to_anchor=(1, 1), loc='upper left')
            plt.xlabel('Date de début')
            plt.ylabel('valeur')
            sns.despine(fig=fig, ax=ax)
            st.pyplot(fig)

    df_sorted = df.sort_values(df.keys()[1], ascending=True)
    fig, ax = plt.subplots(figsize=(10, 5.2))
    for i, (series_name, series) in enumerate(df_sorted.groupby(df.keys()[1])):
        _plot_series(series, series_name, i, target="valeur")
    plt.legend(title='Date de fin', bbox_to_anchor=(1, 1), loc='upper left')
    plt.xlabel('Date de fin')
    plt.ylabel('valeur')
    sns.despine(fig=fig, ax=ax)
    st.pyplot(fig)

    col10,col11=st.columns((2))

    with col10:
        df_sorted = df.sort_values(df.keys()[0], ascending=True)
        fig, ax = plt.subplots(figsize=(10, 5.2))
        for i, (series_name, series) in enumerate(df_sorted.groupby(df.keys()[1])):
            _plot_series(series, series_name, i, target="valeur brute")
        plt.legend(title='Date de début', bbox_to_anchor=(1, 1), loc='upper left')
        plt.xlabel('Date de début')
        plt.ylabel('valeur brute')
        sns.despine(fig=fig, ax=ax)
        st.pyplot(fig)
    
    with col11:
        df_sorted = df.sort_values(df.keys()[1], ascending=True)
        fig, ax = plt.subplots(figsize=(10, 5.2))
        for i, (series_name, series) in enumerate(df_sorted.groupby(df.keys()[1])):
            _plot_series(series, series_name, i, target="valeur brute")
        plt.legend(title='Date de fin', bbox_to_anchor=(1, 1), loc='upper left')
        plt.xlabel('Date de fin')
        plt.ylabel('valeur brute')
        sns.despine(fig=fig, ax=ax)
        st.pyplot(fig)



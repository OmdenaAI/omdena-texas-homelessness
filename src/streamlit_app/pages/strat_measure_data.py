import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.express as px
from pathlib import Path
import seaborn as sns
import os


def app():

    st.title("Strategic Measure of Persons Experiencing Homelessness PIT Counts in Texas")
    #import our data
    strat_df1 = os.path.join(Path(__file__).parents[1],
                             "data/strat_measure_of_persons_experiencing_homelessness_pit_counts.csv")
    strat_df1 = pd.read_csv(strat_df1)                         
    strat_df = strat_df1.drop(["Unnamed: 0"], axis = 1)
    st.write(strat_df.head())
    st.markdown('Visualize the Heatmap, lineplot and Bar Chart of Texas Income-Poverty-Stats Data!')

    selected_features = st.selectbox('Information to visualize?', ['Feature Plots'])

    selected_x_var = st.selectbox('What do you want the x variable to be?', ['unsheltered', 'pit_count_year', 'difference_from_previous_year'])

    selected_y_var = st.selectbox('What do you want the y variable to be?', ['sheltered', 'unsheltered', 'total_unduplicated_individuals'])

    chart_visual = st.sidebar.selectbox("Select Charts/Plot type", ('HeatMap', 'Scatterplot Chart', 'Bar Chart'))             
    fig = go.Figure()

    if chart_visual == "HeatMap":
        st.markdown("## Heatmap")
        fig,ax = plt.subplots()
        sns.heatmap(strat_df.corr(), annot = True, ax =ax, cmap="seismic_r")
        st.write(fig)

    if chart_visual == 'Line Chart':
        fig.add_trace(go.Line(x = strat_df[selected_x_var], y = strat_df[selected_y_var] , mode = 'lines'))

    elif chart_visual == 'Bar Chart':
        fig.add_trace(go.Bar(x = strat_df[selected_x_var] , y = strat_df[selected_y_var]))
        st.plotly_chart(fig, use_container_width=True)

    fig, ax = plt.subplots()
    ax = sns.scatterplot(x = strat_df[selected_x_var], y = strat_df[selected_y_var])
    plt.xlabel(selected_x_var)
    plt.ylabel(selected_y_var)
    st.pyplot(fig)
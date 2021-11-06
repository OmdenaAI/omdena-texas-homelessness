import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.express as px
from pathlib import Path
import seaborn as sns
import os



st.title("Visualization of Income Poverty Statistics from Texas at the County Level")
#import our data
filepath = os.path.join(Path(__file__).parents[1],
                        'data/texas_income_poverty_stats.csv')
texas_df1 = pd.read_csv(filepath)
texas_df = texas_df1.drop(["county"], axis = 1)
st.markdown('Visualizations in the form of Heatmap, Scatterplot and Bar Chart of the Income Poverty Data in Texas.')
selected_features = st.selectbox('What information would you like to visualize?', ['Correlating Features Plots'])
selected_x_var = st.selectbox('What do want the x variable to be?', ['percentage_of_population_in_poverty', 'median_household_income'])
selected_y_var = st.selectbox('What about the y?', ['percentage_of_population_under_18_in_poverty'])
chart_visual = st.sidebar.selectbox("Select Charts/Plot type", ('HeatMap', 'Line Chart', 'Bar Chart'))             
fig = go.Figure()
if chart_visual == "HeatMap":
    st.markdown("## Heatmap")
    st.markdown("Correlation matrix representing the correlation values of each feature within the data to one another")
    fig,ax = plt.subplots()
    sns.heatmap(texas_df.corr(), annot = True, ax =ax, cmap="seismic_r")
    st.write(fig)
if chart_visual == 'Scatter Plot':
    st.markdown("")
    fig, ax = plt.subplots()
    ax = sns.scatterplot(x = texas_df[selected_x_var], y = texas_df[selected_y_var])
    plt.xlabel(selected_x_var)
    plt.ylabel(selected_y_var)
    st.pyplot(fig)
    
elif chart_visual == 'Bar Chart':
    fig.add_trace(go.Bar(x = texas_df[selected_x_var] , y = texas_df[selected_y_var]))
    st.plotly_chart(fig, use_container_width=True)
"""
I cmmented out these lines as the chart should be shown on it's own tab.
Noton every part of this dashboard. This is unnecessary with your line chart.
"""
import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.express as px
from pathlib import Path
import seaborn as sns

st.title("Texas Income-Poverty-Stats Visualization")
#import our data
texas_df1 = pd.read_csv('C:/Users/SALAKO/dlib/omdena-texas-homelessness/src/tasks/task-3-model/data/IncomePovertyStats_Texas.csv')
texas_df = texas_df1.drop(["County", "Number"], axis = 1)
st.write(texas_df.head())
st.markdown('App to visualize the Heatmap, scatterplot and Bar Chart of Texas Income-Poverty-Stats Data!')

selected_features = st.selectbox('What information would you like to visualize?', ['Correlating features Plots'])

selected_x_var = st.selectbox('What do want the x variable to be?', ['% of Population in Poverty', 'Median Household Income'])

selected_y_var = st.selectbox('What about the y?', ['% of Population Under 18 in Poverty'])

chart_visual = st.sidebar.selectbox("Select Charts/Plot type", ('HeatMap', 'Scatterplot Chart', 'Bar Chart'))             
fig = go.Figure()

if chart_visual == "HeatMap":
    st.markdown("## Heatmap")
    fig,ax = plt.subplots()
    sns.heatmap(texas_df.corr(), annot = True, ax =ax, cmap="seismic_r")
    st.write(fig)
    
if chart_visual == 'Line Chart':
    fig.add_trace(go.Line(x = texas_df[selected_x_var], y = texas_df[selected_y_var] , mode = 'lines'))
    
elif chart_visual == 'Bar Chart':
    fig.add_trace(go.Bar(x = texas_df[selected_x_var] , y = texas_df[selected_y_var]))
    st.plotly_chart(fig, use_container_width=True)

fig, ax = plt.subplots()
ax = sns.scatterplot(x = texas_df[selected_x_var], y = texas_df[selected_y_var])
plt.xlabel(selected_x_var)
plt.ylabel(selected_y_var)
st.pyplot(fig)
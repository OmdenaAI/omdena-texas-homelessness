import streamlit as st
import pandas as pd
import seaborn as sns
import plotly.graph_objects as go
import matplotlib.pyplot as plt
from pathlib import Path
import os

def app():
    filepath = os.path.join(Path(__file__).parents[1],
                            'data/needs_met_by_outreach_teams.csv')
    df = pd.read_csv(filepath)
    st.title("Needs met by Outreach Teams")
    st.markdown("The dashboard displays information pertaining to different categories of \
        homeless needs met by outreach teams within Texas")
    st.sidebar.title("Select Visual Charts")
    st.sidebar.markdown("Select a Chart/Plot from the list:")
    chart_visual = st.sidebar.selectbox("Select Charts/Plot type", 
                                        ('Bar Chart', 'HeatMap'))
    st.sidebar.checkbox("Show Analysis by Met Reach", True, key = 1)               
    fig = go.Figure()
    gender = ['fiscal_year','need_type','number_of_needs_met']
    if chart_visual == "HeatMap":
        st.markdown("## Heatmap")
        fig, ax = plt.subplots()
        sns.heatmap(df.corr(), ax =ax, cmap="Blues")
        st.write(fig)
        
    elif chart_visual == 'Bar Chart':
        fig.add_trace(go.Bar(x=df.need_type,
                             y=df.number_of_needs_met,
                             name='number_of_needs_met'))
        # Fixed display issue with Heatmap by returning value inside if statement
        st.plotly_chart(fig, use_container_width=True)
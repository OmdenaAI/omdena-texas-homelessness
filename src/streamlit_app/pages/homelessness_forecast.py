import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import plotly.graph_objects as go
import matplotlib.pyplot as plt
from pathlib import Path
import os

def app():
    filepath = os.path.join(Path(__file__).parents[1],
                            'data/homelessness_forecast.csv')
    vdf = pd.read_csv(filepath)
    # st.title("Forecast of People affected by Homelessness during Jan-2020 to Present (Sept-2021).")
    st.markdown("""The future forecasts can be helpful to NGO's or State Government 
                    to plan appropiate shelters or beds required""")

    fig = go.Figure([
        go.Scatter(name='People Homeless', 
                   x=vdf['Date'], y=vdf['Overall Homeless']),

        go.Scatter(name='Upper Bound',
                   x=vdf['Date'], y=vdf['yhat_upper'],
                   mode='lines', marker=dict(color="#444"),
                   line=dict(width=0), showlegend=False),

        go.Scatter(name='Lower Bound',
                   x=vdf['Date'], y=vdf['yhat_lower'],
                   marker=dict(color="#444"), line=dict(width=0),
                   mode='lines', fillcolor='rgba(68, 68, 68, 0.3)',
                   fill='tonexty', showlegend=False)      
                   ])
                   
    fig.update_layout(
                    yaxis_title='PIT Estimates of Homeless people',
                    title='Trend of Homeless people in Texas in recent years, Forecasted from Jan-2020 to Sept-2021.',
                    hovermode="x"
                    )

    st.plotly_chart(fig, use_container_width=True)
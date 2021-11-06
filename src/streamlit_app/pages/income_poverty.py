import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from pathlib import Path
import os

def app():

    st.title("Income Poverty Statistics in Texas by County")
    st.markdown(" Visualizations of Income Poverty in Texas by County")
    st.sidebar.title("Select Visual Charts")
    st.sidebar.markdown("Select a Chart/Plot from the list:")

    filepath = os.path.join(Path(__file__).parents[1], 
                             'data/texas_income_poverty_stats.csv')
    data = pd.read_csv(filepath)

    chart_visual = st.sidebar.selectbox("Select Charts/Plot Type", 
                                        ("Line Chart", "Bar Chart", "Scatter Plot"))

    st.sidebar.checkbox("Show Analysis by Category", True, key=1)
    selected_status = st.sidebar.selectbox("Select a Category",
                                           options = ['Total Personal Income', 'Median Household Income',
                                                      'Average Annual Pay',
                                                      'Percentage of Population in Poverty',
                                                      'Percentage of Population Under 18 in Poverty'])

    
    fig = go.Figure()

    if chart_visual == "Line Chart":
        if selected_status == "Total Personal Income":
            st.markdown("This graph helps to represent the total amount of income \
                each individual makes by county in Texas. Highlights in this data would \
                    indicate a larger amount of income flowing into that county.")
            fig.add_trace(go.Scatter(x = data.county,
                                     y = data.total_personal_income,
                                     name = 'Total Personal Income by County in Texas',
                                     mode= 'lines'))
        if selected_status == "Median Household Income":
            st.markdown("This graph represents the average household income by county \
                in Texas. Highlights in this data would indicate a larger household income \
                    within that county.")
            fig.add_trace(go.Scatter(x = data.county,
                                     y = data.median_household_income,
                                     name = 'Median Household Income by County in Texas',
                                     mode = 'lines'))
        if selected_status == "Average Annual Pay":
            st.markdown("This graph represents the average annual salaries within counties of Texas. \
                Highlights in this data would represent a higher annual pay within that county.")
            fig.add_trace(go.Scatter(x = data.county,
                                     y = data.average_annual_pay,
                                     name = 'Average Annual Income by County in Texas',
                                     mode = 'lines'))
        if selected_status == "Percentage of Population in Poverty":
            st.markdown("This graph represents the percentage of the population living within poverty guidelines \
                by county in Texas. Highlights in this data would indicate counties where the populous has higher risks of being homeless")
            fig.add_trace(go.Scatter(x = data.county,
                                     y = data.percentage_of_population_in_poverty,
                                     name = 'Percentage of the Population Living in Poverty by County in Texas',
                                     mode = 'lines'))
        if selected_status == "Percentage of Population Under 18 in Poverty":
            st.markdown("This graph represents the percentage of the population that is under the age of 18 living within poverty \
                guidelines by county in Texas. Highlights in this data would indicate counties where the populous has higher risks of being \
                    homeless.")
            fig.add_trace(go.Scatter(x = data.county,
                                     y = data.percentage_of_population_under_18_in_poverty,
                                     name = 'Percentage of Population Under 18 Living in Poverty by County in Texas',
                                     mode = 'lines'))

    if chart_visual == "Bar Chart":
        if selected_status == "Total Personal Income":
            st.markdown("This graph helps to represent the total amount of income \
                each individual makes by county in Texas. Highlights in this data would \
                    indicate a larger amount of income flowing into that county.")
            fig = px.bar(data, x = 'county', y = 'total_personal_income',
                         title = 'Total Personal Income by County in Texas',
                         width = 800, height= 800)

        if selected_status == "Median Household Income":
            st.markdown("This graph represents the average household income by county \
                in Texas. Highlights in this data would indicate a larger household income \
                    within that county.")
            fig = px.bar(data, x = 'county', y = 'median_household_income',
                         title = 'Median Household Income by County in Texas',
                         width = 2000, height= 800)

        if selected_status == "Average Annual Pay":
            st.markdown("This graph represents the average annual salaries within counties of Texas. \
                Highlights in this data would represent a higher annual pay within that county.")
            fig.add_trace(go.Bar(x = data.county,
                                 y = data.average_annual_pay,
                                 name = 'Average Annual Income by County in Texas'))
        if selected_status == "Percentage of Population in Poverty":
            st.markdown("This graph represents the percentage of the population living within poverty guidelines \
                by county in Texas. Highlights in this data would indicate counties where the populous has higher risks of being homeless")
            fig.add_trace(go.Bar(x = data.county,
                                 y = data.percentage_of_population_in_poverty,
                                 name = 'Percentage of the Population Living in Poverty by County in Texas'))
        if selected_status == "Percentage of Population Under 18 in Poverty":
            st.markdown("This graph represents the percentage of the population that is under the age of 18 living within poverty \
                guidelines by county in Texas. Highlights in this data would indicate counties where the populous has higher risks of being \
                    homeless.")
            fig.add_trace(go.Bar(x = data.county,
                                 y = data.percentage_of_population_under_18_in_poverty,
                                 name = 'Percentage of Population Under 18 Living in Poverty by County in Texas'))

    if chart_visual == "Scatter Plot":
        if selected_status == "Total Personal Income":
            st.markdown("This graph helps to represent the total amount of income \
                each individual makes by county in Texas. Highlights in this data would \
                    indicate a larger amount of income flowing into that county.")
            fig = px.scatter(data, x = 'county', y = 'total_personal_income',
                             hover_name= 'county',
                             title = 'Total Personal Income by County in Texas',
                             width = 800, height= 800)
        if selected_status == "Median Household Income":
            st.markdown("This graph represents the average household income by county \
                in Texas. Highlights in this data would indicate a larger household income \
                    within that county.")
            fig = px.scatter(data, x = 'county', y = 'average_annual_pay',
                             title = "Median Household Income by County in Texas",
                             width = 800, height= 800)
            
        if selected_status == "Average Annual Pay":
            st.markdown("This graph represents the average annual salaries within counties of Texas. \
                Highlights in this data would represent a higher annual pay within that county.")
            fig = px.scatter(data, x = 'county', y = 'average_annual_pay',
                             title = 'Average Annual Income by County in Texas',
                             width = 800, height= 800)

        if selected_status == "Percentage of Population in Poverty":
            st.markdown("This graph represents the percentage of the population living within poverty guidelines \
                by county in Texas. Highlights in this data would indicate counties where the populous has higher risks of being homeless")
            fig = px.scatter(data, x = 'county', y = 'percentage_of_population_living_in_poverty',
                             title = 'Percentage of the Population Living in Poverty by County in Texas',
                             width = 800, height= 800)

        if selected_status == "Percentage of Population Under 18 in Poverty":
            st.markdown("This graph represents the percentage of the population that is under the age of 18 living within poverty \
                guidelines by county in Texas. Highlights in this data would indicate counties where the populous has higher risks of being \
                    homeless.")
            fig = px.scatter(data, x = 'county', y ='percentage_of_population_under_18_in_poverty',
                             title = 'Percantge of Population Under 18 Living in Poverty by County in Texas',
                             width = 800, height= 800)


    st.plotly_chart(fig, use_container_width=True)
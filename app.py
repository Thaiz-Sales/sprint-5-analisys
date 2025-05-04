import pandas as pd
import plotly.express as px
import streamlit as st

# data reading
car_data = pd.read_csv('./data/vehicles.csv')

# creates a histogram's button
hist_button = st.button('Create histogram')

# if button hited
if hist_button:
    # show message
    st.write('Creating a histogram')

    # create a histogram
    fig_hist = px.histogram(car_data, x = "odometer",title = 'Vehicle Mileage Distribution')

    # Shows histogram
    st.plotly_chart(fig_hist, use_container_width=True)

# create a checkbox for the scatter plot
build_scatter = st.checkbox('Create a scatter plot')

# if the checkbox is selected
if build_scatter:
    st.write('Creating a Scatter Plot - Comparison between mileage and price')

    # Create a scatter plot
    fig_scatter = px.scatter(car_data, x="odometer", y="price",title = 'Vehicle Mileage X price')

    # display the interactive Plotly scatter plot
    st.plotly_chart(fig_scatter, use_container_width=True)

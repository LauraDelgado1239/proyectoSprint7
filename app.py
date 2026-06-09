import pandas as pd
import plotly.express as px
import streamlit as st

df = pd.read_csv('vehicles_us.csv')

st.header('US Vehicle Listings — Data Explorer')

st.subheader('Price Distribution')
price_hist = st.checkbox('Show price histogram', value=True)
if price_hist:
    fig = px.histogram(df, x='price', nbins=50, range_x=[0, 100000],
                       title='Distribution of Vehicle Prices',
                       labels={'price': 'Price (USD)'})
    st.plotly_chart(fig, use_container_width=True)

st.subheader('Price vs Odometer')
scatter = st.checkbox('Show scatter plot', value=True)
if scatter:
    fig = px.scatter(df, x='odometer', y='price', color='condition',
                     range_y=[0, 100000], opacity=0.4,
                     title='Price vs Odometer by Condition',
                     labels={'odometer': 'Odometer (miles)', 'price': 'Price (USD)'})
    st.plotly_chart(fig, use_container_width=True)

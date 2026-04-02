



import pandas as pd
import streamlit as st

df=pd.read_csv('retail_data (1).csv')
df['Order_Date']=pd.to_datetime(df['Order_Date'])
st.title('Retail Sales Dashboard')
st.subheader('Key Matrices')
col1, col2, col3=st.columns(3)
col1.metric('Total Revenue',df['Revenue'].sum())
col2.metric('Total Orders',df['Order_ID'].nunique())
col3.metric('Average Order Value',round(df['Revenue'].mean(),2))

# Region Filter
region=st.selectbox("Select Region",df['Region'].unique())
filtered_df=df[df['Region']==region]

st.write("Filtered Data",filtered_df)

# Bar Plot 
st.subheader("Sales by Category")
st.bar_chart(filtered_df.groupby('Category')['Revenue'].sum())

# Monthly Trends
st.subheader("Monthly Sales Trend")
df['Month']=df['Order_Date'].dt.to_period('M').astype(str)
st.line_chart(df.groupby('Month')['Revenue'].sum())
import pandas as pd

import streamlit as st
df=pd.read_csv("retail_data (1).csv")
df['Order_Date']=pd.to_datetime(df['Order_Date'])
st.title('Retail sales dashboard')
st.subheader('key matrices')
col1,col2,col3=st.columns(3)
col1.metric("Total Revenue",df['Revenue'].sum())
col2.metric("Total Order",df['Order_ID'].count())
col3.metric("Average Order Value",round(df['Revenue'].mean(),2))
import pandas as pd
import streamlit as st
import numpy as np

df = pd.read_csv('student_performance.csv')

# 🔥 Fix: convert to numeric
df['Final_Score'] = pd.to_numeric(df['Final_Score'], errors='coerce')
df['Attendance'] = pd.to_numeric(df['Attendance'], errors='coerce')

st.title("Student Performance Analyzer")
st.subheader('Key Matrices')

col1, col2, col3 = st.columns(3)

col1.metric('Total Students Enrolled', df['Student_ID'].count())
col2.metric('Average Result of students', round(df['Final_Score'].mean(), 2))
col3.metric('Average attendance of students', round(df['Attendance'].mean(), 2))

# filter by gender
region = st.selectbox("Select Gender", df['Gender'].unique())
filtered_df = df[df['Gender'] == region]

st.write("Filtered Data", filtered_df)
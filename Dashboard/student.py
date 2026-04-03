
import pandas as pd
import streamlit as st
import numpy as np

df=pd.read_csv('student_performance.csv')
st.title("Student Performance Analyzer")
st.subheader('Key Matrices')
col1,col2,col3=st.columns(3)
#student performance by column
col1.metric('Total Students Endrolled',df['Student_ID'].count())
col2.metric('Average Result of students',df['Final_Score'].mean())
col3.metric('Average attendence of students',df['Attendance'].mean())
#student details according to their dender

region=st.selectbox("Select Region",df['Gender'].unique())
filtered_df=df[df['Gender']== region]
st.write("Filtered Data",filtered_df)
import streamlit as st
import pickle 
import warnings
warnings.filterwarnings("ignore")

st.header("weather prediction")
pt=st.number_input("Enter precipitation here: ")
t_max=st.number_input("Enter mximum temperature: ")
t_min=st.number_input("Enter minimum temperature: ")
wind=st.number_input("Enter wind speed: ")
btn=st.button("predict")

if btn:
    model=pickle.load(open("wp.pkl","rb"))
    res=model.predict([[pt,t_max,t_min,wind]])[0]
    st.markdown(f"Expected weather: {res}")
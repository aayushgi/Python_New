import streamlit as st
import pickle
import warnings 
warnings.filterwarnings("ignore")
st.header("House price prediction")
size=st.number_input("Enter size of the land: ")
bed=st.number_input("Enter number of beadrooms: ")
age=st.number_input("Enter how old is your house: ")
dist=st.number_input("Enter the distance from city: ")
btn=st.button("predict")
if btn:
    with open("hpp.pkl", "rb") as f:
        model= pickle.load(f)
    res=model.predict([[size,bed,age,dist]])[0]
    res=round(res,2)
    st.markdown(f"Approximate prize {res}")

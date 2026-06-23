import streamlit as st
import pickle
import numpy as np

# Load model and scaler
model = pickle.load(open("loan_model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))

st.set_page_config(page_title="Credit Wise Loan System", page_icon="🏦")

st.title("🏦 Credit Wise Loan System")
st.markdown("### Check Your Loan Approval Eligibility")

# Numeric Inputs
Applicant_Income = st.number_input("Applicant Income", min_value=0.0)
Coapplicant_Income = st.number_input("Coapplicant Income", min_value=0.0)
Age = st.number_input("Age", min_value=18.0)
dependents = st.selectbox(
    "Number of Dependents on you",
    ["0", "1", "2", "3+"]
)

if dependents == "3+":
    Dependents = 3
else:
    Dependents = int(dependents)
Credit_Score = st.number_input("Credit Score", min_value=300.0, max_value=900.0)
Existing_Loans = st.selectbox(
    "Existing Loans",
    [0, 1, 2, 3, 4, 5]
)
DTI_Ratio = st.slider(
    "How much of your income goes to loan EMI?",
    min_value=0.0,
    max_value=1.0,
    value=0.30
)
Savings = st.number_input("Savings", min_value=0.0)
Collateral_Value = st.number_input(
    "Property Value (₹)",
    min_value=0.0
)
Loan_Amount = st.number_input("Loan Amount", min_value=0.0)
Loan_Term = st.selectbox(
    "Loan Term (Months)",
    [12, 24, 36, 60, 120, 180, 240, 360]
)
education = st.selectbox(
    "Education Level",
    ["High School", "Graduate", "Post Graduate", "PhD"]
)

education_map = {
    "High School": 0,
    "Graduate": 1,
    "Post Graduate": 2,
    "PhD": 3
}

Education_Level = education_map[education]

st.markdown("---")

employment = st.selectbox(
    "Employment Status",
    ["Salaried", "Self-employed", "Unemployed"]
)

Employment_Status_Salaried = 1 if employment == "Salaried" else 0
Employment_Status_Self_employed = 1 if employment == "Self-employed" else 0
Employment_Status_Unemployed = 1 if employment == "Unemployed" else 0


marital = st.selectbox(
    "Marital Status",
    ["Single", "Married"]
)

Marital_Status_Single = 1 if marital == "Single" else 0


purpose = st.selectbox(
    "Loan Purpose",
    ["Car", "Education", "Home", "Personal"]
)

Loan_Purpose_Car = 1 if purpose == "Car" else 0
Loan_Purpose_Education = 1 if purpose == "Education" else 0
Loan_Purpose_Home = 1 if purpose == "Home" else 0
Loan_Purpose_Personal = 1 if purpose == "Personal" else 0


area = st.selectbox(
    "Property Area",
    ["Rural", "Semiurban", "Urban"]
)

Property_Area_Semiurban = 1 if area == "Semiurban" else 0
Property_Area_Urban = 1 if area == "Urban" else 0


gender = st.selectbox(
    "Gender",
    ["Male", "Female"]
)

Gender_Male = 1 if gender == "Male" else 0


employer = st.selectbox(
    "Employer Category",
    ["Government", "MNC", "Private", "Unemployed"]
)

Employer_Category_Government = 1 if employer == "Government" else 0
Employer_Category_MNC = 1 if employer == "MNC" else 0
Employer_Category_Private = 1 if employer == "Private" else 0
Employer_Category_Unemployed = 1 if employer == "Unemployed" else 0

if st.button("Predict Loan Approval"):

    data = np.array([[
        Applicant_Income,
        Coapplicant_Income,
        Age,
        Dependents,
        Credit_Score,
        Existing_Loans,
        DTI_Ratio,
        Savings,
        Collateral_Value,
        Loan_Amount,
        Loan_Term,
        Education_Level,
        Employment_Status_Salaried,
        Employment_Status_Self_employed,
        Employment_Status_Unemployed,
        Marital_Status_Single,
        Loan_Purpose_Car,
        Loan_Purpose_Education,
        Loan_Purpose_Home,
        Loan_Purpose_Personal,
        Property_Area_Semiurban,
        Property_Area_Urban,
        Gender_Male,
        Employer_Category_Government,
        Employer_Category_MNC,
        Employer_Category_Private,
        Employer_Category_Unemployed
    ]])

    scaled_data = scaler.transform(data)
    prediction = model.predict(scaled_data)

    if prediction[0] == 1:
        st.success("✅ Loan Approved")
    else:
        st.error("❌ Loan Rejected")
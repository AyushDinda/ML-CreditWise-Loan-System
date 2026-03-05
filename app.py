import streamlit as st
import pickle
import pandas as pd

# Load model

model = pickle.load(open("loan_model.pkl","rb"))

st.set_page_config(page_title="CreditWise Loan Approval", layout="centered")

st.title("💰 CreditWise Loan Approval Predictor")
st.write(
"""
This tool predicts whether a loan application is likely to be **approved or rejected**
based on financial and personal factors.

⚠️ **Note:** This prediction is only based on a machine learning model and should not be used as real financial advice.
"""
)

st.header("📋 Applicant Information")

col1, col2 = st.columns(2)

with col1:
    income = st.number_input(
    "Applicant Income (Monthly)",
    help="Your monthly income before tax."
    )
    
    age = st.number_input(
        "Age",
        help="Applicant's current age."
    )
    
    dependents = st.number_input(
        "Number of Dependents",
        help="Family members financially dependent on you."
    )
    
    savings = st.number_input(
        "Total Savings",
        help="Total savings available in bank accounts or deposits."
    )
    
    loan_amount = st.number_input(
        "Loan Amount Requested",
        help="The amount of loan requested from the bank."
    )
    
    credit_score = st.number_input(
        "Credit Score",
        help="Your creditworthiness score (usually between 300 and 850)."
    )
    

with col2:
    co_income = st.number_input(
    "Co-Applicant Income",
    help="Income of co-applicant (if any)."
    )
    
    
    existing_loans = st.number_input(
        "Existing Loans",
        help="Number of loans currently active."
    )
    
    collateral = st.number_input(
        "Collateral Value",
        help="Estimated value of assets used as collateral."
    )
    
    loan_term = st.number_input(
        "Loan Term (Months)",
        help="Duration of loan repayment in months."
    )
    
    dti = st.number_input(
        "Debt-to-Income Ratio",
        help="Percentage of income used to pay debts (0.0 – 1.0)."
    )
    
    education = st.selectbox(
        "Education Level",
        ["Not Graduate", "Graduate"],
        help="Higher education often improves loan approval chances."
    )
    

st.header("🏠 Personal Information")

employment = st.selectbox(
"Employment Status",
["Salaried","Self-employed","Unemployed"]
)

marital = st.selectbox(
"Marital Status",
["Single","Married"]
)

purpose = st.selectbox(
"Loan Purpose",
["Home","Car","Education","Personal"]
)

property_area = st.selectbox(
"Property Area",
["Urban","Semiurban","Rural"]
)

gender = st.selectbox(
"Gender",
["Male","Female"]
)

employer_category = st.selectbox(
"Employer Category",
["Government","MNC","Private","Unemployed"]
)

st.markdown("---")

if st.button("🔎 Predict Loan Approval"):
    data = {
        "Applicant_Income": income,
        "Coapplicant_Income": co_income,
        "Age": age,
        "Dependents": dependents,
        "Existing_Loans": existing_loans,
        "Savings": savings,
        "Collateral_Value": collateral,
        "Loan_Amount": loan_amount,
        "Loan_Term": loan_term,
        "Education_Level": 1 if education=="Graduate" else 0,

        "Employment_Status_Salaried": 1 if employment=="Salaried" else 0,
        "Employment_Status_Self-employed": 1 if employment=="Self-employed" else 0,
        "Employment_Status_Unemployed": 1 if employment=="Unemployed" else 0,

        "Marital_Status_Single": 1 if marital=="Single" else 0,

        "Loan_Purpose_Car": 1 if purpose=="Car" else 0,
        "Loan_Purpose_Education": 1 if purpose=="Education" else 0,
        "Loan_Purpose_Home": 1 if purpose=="Home" else 0,
        "Loan_Purpose_Personal": 1 if purpose=="Personal" else 0,

        "Property_Area_Semiurban": 1 if property_area=="Semiurban" else 0,
        "Property_Area_Urban": 1 if property_area=="Urban" else 0,

        "Gender_Male": 1 if gender=="Male" else 0,

        "Employer_Category_Government": 1 if employer_category=="Government" else 0,
        "Employer_Category_MNC": 1 if employer_category=="MNC" else 0,
        "Employer_Category_Private": 1 if employer_category=="Private" else 0,
        "Employer_Category_Unemployed": 1 if employer_category=="Unemployed" else 0,

        "DTI_Ratio_sq": dti**2,
        "Credit_Score_sq": credit_score**2
    }

    df = pd.DataFrame([data])

    prediction = model.predict(df)
    probability = model.predict_proba(df)

    st.subheader("📊 Prediction Result")

    if prediction[0] == 1:
        st.success("✅ Loan Approved")
    else:
        st.error("❌ Loan Not Approved")

    st.write("### Confidence")
    st.write(f"Approval Probability: **{probability[0][1]*100:.2f}%**")

st.markdown("---")

st.subheader("📘 How This Prediction Works")
st.write(
"""
The model considers multiple financial factors such as:
- Income levels
- Credit score
- Existing loans
- Savings
- Debt-to-income ratio
- Employment status
- Loan purpose

Higher income, better credit score, and lower debt usually increase the chances of approval.
"""
)


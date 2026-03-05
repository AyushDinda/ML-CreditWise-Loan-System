# 💰 CreditWise Loan Approval System

A Machine Learning web application that predicts whether a loan application is likely to be **approved or rejected** based on financial and personal information.

This project uses **Python, Scikit-learn, and Streamlit** to build an interactive interface where users can enter their details and receive a prediction instantly.

---

## 🚀 Live Application

Run locally using Streamlit:

```bash
python -m streamlit run app.py
```

---

# 📊 Project Overview

Banks evaluate multiple factors before approving loans.
This project simulates that process using a **machine learning classification model**.

The model analyzes information such as:

* Applicant income
* Co-applicant income
* Credit score
* Savings
* Loan amount
* Debt-to-income ratio
* Employment status
* Loan purpose
* Property area
* Employer category

Based on these factors, the system predicts:

✅ **Loan Approved**
❌ **Loan Not Approved**

---

# 🧠 Machine Learning Workflow

The project follows a complete ML pipeline:

1. Data Cleaning
2. Missing Value Handling
3. Exploratory Data Analysis (EDA)
4. Feature Encoding
5. Feature Engineering
6. Train-Test Split
7. Feature Scaling
8. Model Training
9. Model Evaluation

### Models Tested

* Logistic Regression
* K-Nearest Neighbors (KNN)
* Gaussian Naive Bayes

The **Naive Bayes model** showed strong performance and was used for deployment.

---

# 🛠 Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Matplotlib
* Seaborn
* Streamlit

---

# 🖥 Streamlit Web Interface

The Streamlit interface allows users to input their financial details and instantly see the predicted loan approval result along with model confidence.

Features include:

* Interactive UI
* Explainable inputs
* Approval probability display
* Clean financial data form

---

# 📌 Demo Scenarios

## ✅ Scenario 1 — Loan Approved

Example input:

| Feature             | Value    |
| ------------------- | -------- |
| Applicant Income    | 12000    |
| Co-Applicant Income | 5000     |
| Age                 | 38       |
| Dependents          | 2        |
| Savings             | 20000    |
| Loan Amount         | 15000    |
| Credit Score        | 745      |
| Existing Loans      | 0        |
| Collateral Value    | 30000    |
| Loan Term           | 36       |
| DTI Ratio           | 0.22     |
| Education           | Graduate |
| Employment Status   | Salaried |
| Loan Purpose        | Home     |

### Result

```
Loan Approved
```

Reason:

* Strong income
* High credit score
* Good savings
* Low debt ratio

---

## ❌ Scenario 2 — Loan Rejected

Example input:

| Feature             | Value        |
| ------------------- | ------------ |
| Applicant Income    | 3000         |
| Co-Applicant Income | 0            |
| Age                 | 24           |
| Dependents          | 3            |
| Savings             | 800          |
| Loan Amount         | 12000        |
| Credit Score        | 540          |
| Existing Loans      | 2            |
| Collateral Value    | 1500         |
| Loan Term           | 12           |
| DTI Ratio           | 0.68         |
| Education           | Not Graduate |
| Employment Status   | Unemployed   |
| Loan Purpose        | Personal     |

### Result

```
Loan Not Approved
```

Reason:

* Low income
* Poor credit score
* High debt-to-income ratio
* No collateral

---

# 📂 Project Structure

```
CreditWiseLoanApprovalSystem
│
├── app.py
├── loan_model.pkl
├── dataset.csv
├── notebook.ipynb
├── requirements.txt
└── README.md
```

---

# 🎯 Future Improvements

* Add SHAP explanations for model predictions
* Improve feature importance visualization
* Deploy application on Streamlit Cloud
* Add more advanced models like Random Forest or XGBoost

---

# 👨‍💻 Author

**Ayush Dinda**

Machine Learning & Software Development Enthusiast
B.Tech Student

---

⭐ If you found this project useful, consider giving it a star!

# 📞 Telco Customer Churn Prediction (Deployed Machine Learning Project)

## 🔍 Project Overview

Customer churn is a major problem in the telecom industry. Acquiring a new customer costs **5–7× more** than retaining an existing one.
This project builds an end-to-end Machine Learning system that predicts whether a telecom customer is likely to leave the company and provides a **churn risk probability**.

The system is deployed as an interactive web application where a user can enter customer details and instantly receive a prediction.

---

## 🎯 Objective

To develop a production-style ML pipeline that:

* Detects customers at risk of leaving (churn)
* Handles imbalanced data
* Provides probability-based decision support
* Is accessible through a live web interface

---

## 🚀 Live Application

👉 *(Paste your Render deployment link here)*

---

## 🧠 Machine Learning Approach

### Dataset

* Telco Customer Churn Dataset (IBM Sample Dataset)
* ~7,000 telecom customers
* Includes demographics, subscription plans, billing, and service usage

### Key Challenges

* Imbalanced classes (≈ 73% stay, 27% churn)
* Mixed categorical + numerical features
* Real-world deployment requirement

### Solution

* Built a preprocessing pipeline using **ColumnTransformer**
* Applied **OneHotEncoding** for categorical variables
* Handled missing values using **SimpleImputer**
* Solved class imbalance using **class_weight='balanced'**
* Used **Random Forest Classifier**
* Implemented probability-based threshold (40%) for early churn detection

---

## ⚙️ Model Performance

| Metric          | Score |
| --------------- | ----- |
| Accuracy        | 80%   |
| Churn Recall    | 52%   |
| Churn Precision | 68%   |
| F1 Score        | 0.58  |

The focus was not only accuracy but **detecting churn customers early**, which is more valuable for business retention strategies.

---

## 🧪 Features Used

* Customer tenure
* Contract type
* Internet service type
* Monthly charges
* Payment method
* Tech support
* Online security
* Streaming services
* Paperless billing
* Demographic details

---

## 🖥️ Web Application

The model is deployed using **Streamlit**.

Users can:

1. Enter customer subscription details
2. Click Predict
3. Receive:

   * Churn Risk Probability
   * Stay/Leave Decision

---

## 🏗️ Project Structure

```
telco-churn-prediction/
│
├── app.py
├── telco_churn_model.joblib
├── requirements.txt
├── README.md
├── 1_EDA_Preprocessing.ipynb
└── 2_Model_Training_and_Export.ipynb
```

---

## 🛠️ Tech Stack

* Python
* Pandas
* NumPy
* Scikit-learn
* Streamlit
* Joblib
* GitHub
* Render (deployment)

---

## 📊 How to Run Locally

```bash
git clone https://github.com/yourusername/telco-churn-prediction.git
cd telco-churn-prediction

pip install -r requirements.txt
streamlit run app.py
```

---

## 💡 Business Impact

The system helps telecom companies:

* Identify high-risk customers early
* Offer retention incentives
* Reduce revenue loss
* Improve customer lifetime value

---

## 📌 Key Learning Outcomes

* Built an end-to-end ML pipeline
* Worked with imbalanced datasets
* Implemented cost-sensitive learning
* Saved & loaded models using joblib
* Deployed ML model as a web application
* Converted a notebook model into a production-ready system

---

## 👨‍💻 Author

**Kshitij Joshi**

If you found this useful, consider giving the repository a ⭐


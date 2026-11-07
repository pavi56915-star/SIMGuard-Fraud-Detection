# 📱 SIMGuard – SIM Fraud Detection System

### Machine Learning Based SIM Fraud Risk Assessment

A web-based application that uses Machine Learning to identify suspicious SIM card activities and estimate the probability of SIM fraud based on customer and usage-related information.

## 📌 Project Overview

The SIMGuard SIM Fraud Detection System helps identify potentially fraudulent SIM cards using customer details and SIM usage patterns such as call count, SMS count, data usage, unique locations, unique devices, and international calls.

The application estimates fraud probability, assigns risk levels, and provides appropriate actions to help identify suspicious SIM activities.

## 🎯 Objectives

- Detect potentially fraudulent SIM activities.
- Estimate SIM fraud probability.
- Identify low, medium, and high fraud-risk levels.
- Provide understandable risk indicators.
- Support SIM fraud assessment.
- Evaluate Machine Learning model performance.
- Provide a user-friendly fraud detection dashboard.

## 🛠️ Technologies Used

| **Category** | **Technologies** |
|---|---|
| Programming Language | Python |
| Machine Learning | Scikit-learn |
| Algorithm | Logistic Regression |
| Backend | Flask |
| Frontend | HTML, CSS |
| Data Processing | Pandas, NumPy |
| Model Deployment | Flask, Joblib |

## 📊 Dataset Details

The model uses the following input features:

- Age
- Call Count
- SMS Count
- Data Usage (GB)
- Unique Locations
- Unique Devices
- Recharge Count
- International Calls
- SIM Age (Days)

**Target Variable:** `Fraud_Label`

The target indicates whether a SIM card is fraudulent or normal.

- 0 – Normal SIM
- 1 – Fraud SIM

## 🤖 Machine Learning Algorithm

**Logistic Regression**

Logistic Regression is a supervised Machine Learning classification algorithm used to predict the probability of a binary outcome.

It is suitable for this project because the target variable has two classes:

- 0 – Normal SIM
- 1 – Fraud SIM

The model estimates the probability of SIM fraud based on customer information and SIM usage patterns.

## ⚙️ Application Modules

### 1. SIM Fraud Assessment

- Enter SIM and customer details.
- Analyze SIM usage information.
- Estimate fraud probability.
- Generate a risk score.

### 2. Risk Classification

The system classifies SIM cards into three risk levels:

- **Low Risk (0–30):** Normal SIM – Allow SIM.
- **Medium Risk (31–60):** Suspicious SIM – Review SIM.
- **High Risk (61–100):** Fraud SIM – Block SIM and send for verification.

### 3. Fraud Detection Dashboard

- Display fraud probability.
- Show risk score out of 100.
- Display risk classification.
- Show prediction results.
- Provide recommended actions.

## 📈 Model Performance

| **Evaluation Metric** | **Result** |
|---|---|
| Accuracy | 87.6% |

The model achieved 87.6% accuracy during evaluation on the test dataset.

## 🔄 Project Workflow

1. Dataset Collection
2. Data Preprocessing
3. Handling Missing Values
4. Feature Selection
5. Train-Test Splitting (80:20)
6. Feature Scaling using StandardScaler
7. Logistic Regression Model Training
8. Model Evaluation
9. Flask Application Development
10. SIM Fraud Risk Prediction
11. Risk Classification and Action Recommendation

## ▶️ How to Run the Project

1. Clone the repository:

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

2. Navigate to the project folder:

```bash
cd SIMGuard
```

3. Install the required libraries:

```bash
pip install flask pandas numpy scikit-learn joblib
```

4. Run the Flask application:

```bash
python app.py
```

5. Open the application in your browser:

```text
http://127.0.0.1:5000
```

## 🔐 Fraud Risk Assessment

The application analyzes SIM usage patterns and generates a fraud probability score to help identify suspicious SIM activities.

## ⚠️ Disclaimer

This system provides estimated SIM fraud probabilities for risk assessment and decision support. It does not guarantee that a SIM card is fraudulent. Final verification should be performed before taking action against a SIM card.

## 👩‍💻 Project Repository

**SIMGuard – SIM Fraud Detection System**

Add your GitHub repository link here.

---

**Developed as an academic Machine Learning project.**

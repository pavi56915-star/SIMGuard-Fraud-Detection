import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

# Load dataset
df = pd.read_csv("dataset.csv")
df.columns = df.columns.str.strip()

# Features
features = [
    "Age", "Call_Count", "SMS_Count", "Data_Usage_GB",
    "Unique_Locations", "Unique_Devices", "Recharge_Count",
    "International_Calls", "SIM_Age_Days"
]
# Prepare data
df = df.dropna(subset=["Fraud_Label"])
X = df[features].fillna(df[features].median())
y = df["Fraud_Label"]

# Training and testing
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)
# Preprocessing
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Train Logistic Regression model
model = LogisticRegression()
model.fit(X_train, y_train)

# Accuracy
accuracy = model.score(X_test, y_test) * 100
print("Model Accuracy:", round(accuracy, 2), "%")

# SIM details
print("\n===== SIM FRAUD ASSESSMENT =====")
sim_id = input("Enter SIM ID: ")
customer_id = input("Enter Customer ID: ")

values = [
    float(input("Age: ")),
    float(input("Call Count: ")),
    float(input("SMS Count: ")),
    float(input("Data Usage (GB): ")),
    float(input("Unique Locations: ")),
    float(input("Unique Devices: ")),
    float(input("Recharge Count: ")),
    float(input("International Calls: ")),
    float(input("SIM Age (Days): "))
]
# Create and scale new SIM
new_sim = pd.DataFrame([values], columns=features)
new_sim = scaler.transform(new_sim)

# Fraud probability
probability = model.predict_proba(new_sim)[0][1]
score = probability * 100

# Risk classification
if score <= 30:
    risk = "LOW"
    prediction = "NORMAL SIM"
    action = "Allow SIM"
elif score <= 60:
    risk = "MEDIUM"
    prediction = "SUSPICIOUS SIM"
    action = "Review SIM"
else:
    risk = "HIGH"
    prediction = "FRAUD SIM"
    action = "Block SIM and send for verification"

# Display result
print("\n===== SIM FRAUD ASSESSMENT  RESULT =====")
print("SIM ID:", sim_id)
print("Customer ID:", customer_id)
print("Fraud Probability:", round(score, 2), "%")
print("Risk Score:", round(score, 2), "/100")
print("Risk Level:", risk)
print("Prediction:", prediction)
print("Action:", action)
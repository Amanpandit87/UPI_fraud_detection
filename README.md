# UPI Fraud Detection using Machine Learning

This project is a **UPI Fraud Detection System** built using machine learning.  
It uses a **Gradient Boosting Classifier (GBM)** trained on a UPI transactions dataset to classify whether a transaction is **fraudulent** or **safe**.

The model has been exported as a `.pkl` file and integrated into a **Streamlit web application** for an interactive user interface.

---

## 📂 Project Structure

├── upi_fraud_dataset.csv # Dataset

├── train_model.py # Model training script

├── grb_upi.pkl # Trained Gradient Boosting Model (saved with pickle)

├── app.py # Streamlit GUI for prediction

├── requirements.txt # Required dependencies

└── README.md # Project documentation


---

## ⚙️ Features

- Preprocessing steps:
  - Removed unusable columns (`Id`, `trans_year`)
  - Selected key features:  
    `trans_hour`, `trans_day`, `trans_month`, `category`, `upi_number`, `trans_amount`

- Trained multiple ML models, finalized **Gradient Boosting Classifier (GRB)**.
- Achieved good accuracy on test data.
- GUI built with **Streamlit** for easy predictions.

---

## 🚀 How to Run

### 1️⃣ Clone Repository

git clone https://github.com/Amanpandit87/UPI_fraud_detection


cd upi-fraud-detection


The app takes the following inputs:

Transaction Hour

Transaction Day

Transaction Month

Category

UPI Number

Transaction Amount

and predicts whether the transaction is Fraud (1) or Safe (0).

# app.py
import streamlit as st
import pandas as pd
import pickle
from sklearn.preprocessing import LabelEncoder

# Load the trained model
with open("grb_upi.pkl", "rb") as f:
    model = pickle.load(f)

st.title("UPI Fraud Risk Prediction")
st.write("Fill the details of the transaction:")

# User inputs
trans_hour = st.number_input("Transaction Hour (0-23)", min_value=0, max_value=23, value=12)
trans_day = st.number_input("Transaction Day (1-31)", min_value=1, max_value=31, value=15)
trans_month = st.number_input("Transaction Month (1-12)", min_value=1, max_value=12, value=6)

# Categories (14 categories)
categories = ['Food', 'Shopping', 'Bill Payment', 'Recharge', 'Transfer', 
              'Entertainment', 'Travel', 'Education', 'Medical', 'Investment', 
              'Gifts', 'Utilities', 'Other', 'Insurance']
category = st.selectbox("Category", categories)

# Encode category
le = LabelEncoder()
le.fit(categories)
category_encoded = le.transform([category])[0]

upi_number = st.text_input("UPI Number (last 4 digits or masked format)", value="1234")
trans_amount = st.number_input("Transaction Amount", min_value=0.0, value=100.0)

if st.button("Predict Fraud Risk"):
    try:
        # Prepare input DataFrame
        input_data = pd.DataFrame({
            'trans_hour':[trans_hour],
            'trans_day':[trans_day],
            'trans_month':[trans_month],
            'category':[category_encoded],
            'upi_number':[int(upi_number)],  # numeric
            'trans_amount':[trans_amount]
        })

        # Make prediction
        prediction = model.predict(input_data)[0]

        # Map numeric output to custom text
        if prediction == 1:
            result_text = "High Risk: Fraudulent Transaction"
            st.markdown(f"<h3 style='color:red'>{result_text}</h3>", unsafe_allow_html=True)
        else:
            result_text = "Low Risk: Legitimate Transaction"
            st.markdown(f"<h3 style='color:green'>{result_text}</h3>", unsafe_allow_html=True)

    except Exception as e:
        st.error(f"Error: {e}")

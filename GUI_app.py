import streamlit as st
import pandas as pd
import pickle
from sklearn.preprocessing import LabelEncoder
import base64

st.set_page_config(page_title="UPI Fraud Detection", layout="wide")

# Function to set local image as background
def set_bg(image_file):
    with open(image_file, "rb") as f:
        data = f.read()
    encoded = base64.b64encode(data).decode()
    page_bg_img = f"""
    <style>
    [data-testid="stAppViewContainer"] {{
        background-image: url("data:image/png;base64,{encoded}");
        background-size: cover;
        background-position: center;
    }}
    .overlay-box {{
        background-color: rgba(0,0,0,0.6);
        padding: 20px;
        border-radius: 15px;
        max-width: 450px;
        margin: auto;
        color: white;
    }}
    </style>
    """
    st.markdown(page_bg_img, unsafe_allow_html=True)

# ⬇️ यहां अपने image file का path डालना है
set_bg("Fraud-Detection-Machine-Learning.jpg")

# Load model
with open("grb_upi.pkl", "rb") as f:
    model = pickle.load(f)

st.title("UPI Fraud Risk Prediction")

# Overlay box start
st.markdown('<div class="overlay-box">', unsafe_allow_html=True)

st.write("Fill the details of the transaction:")

# User inputs
trans_hour = st.number_input("Transaction Hour (0-23)", min_value=0, max_value=23, value=12)
trans_day = st.number_input("Transaction Day (1-31)", min_value=1, max_value=31, value=15)
trans_month = st.number_input("Transaction Month (1-12)", min_value=1, max_value=12, value=6)

categories = ['Food', 'Shopping', 'Bill Payment', 'Recharge', 'Transfer', 
              'Entertainment', 'Travel', 'Education', 'Medical', 'Investment', 
              'Gifts', 'Utilities', 'Other', 'Insurance']
category = st.selectbox("Category", categories)

le = LabelEncoder()
le.fit(categories)
category_encoded = le.transform([category])[0]

upi_number = st.text_input("UPI Number (last 4 digits or masked format)", value="1234")
trans_amount = st.number_input("Transaction Amount", min_value=0.0, value=100.0)

if st.button("Predict Fraud Risk"):
    try:
        input_data = pd.DataFrame({
            'trans_hour':[trans_hour],
            'trans_day':[trans_day],
            'trans_month':[trans_month],
            'category':[category_encoded],
            'upi_number':[int(upi_number)],
            'trans_amount':[trans_amount]
        })

        prediction = model.predict(input_data)[0]

        # Custom output text and color
        if prediction == 1:
            result_text = "High Risk: Fraudulent Transaction"
            st.markdown(f"<h3 style='color:red'>{result_text}</h3>", unsafe_allow_html=True)
        else:
            result_text = "Low Risk: Legitimate Transaction"
            st.markdown(f"<h3 style='color:green'>{result_text}</h3>", unsafe_allow_html=True)

    except Exception as e:
        st.error(f"Error: {e}")

# Overlay box end
st.markdown('</div>', unsafe_allow_html=True)

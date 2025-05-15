
import streamlit as st
import joblib

# Load the model and vectorizer
model = joblib.load("phishing_model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

st.set_page_config(page_title="Phishing Email Detector", page_icon="🛡️")
st.title("🛡️ AI-Powered Phishing Email Detector")
st.write("Paste an email below to check if it's likely phishing or legitimate using an AI model.")

# User input
email_text = st.text_area("✉️ Enter email text here:")

if st.button("🔍 Check Email"):
    if email_text.strip() == "":
        st.warning("Please enter some email text.")
    else:
        input_vec = vectorizer.transform([email_text])
        prediction = model.predict(input_vec)
        result = "🚨 This is likely a **Phishing** email." if prediction[0] == 1 else "✅ This email looks **Legitimate**."
        st.markdown(result)

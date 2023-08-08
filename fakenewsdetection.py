import streamlit as st
import joblib
import numpy as np

# Load the trained model
model = joblib.load("model.pkl")

# Define the Streamlit app
def main():
    st.title("Fake News Prediction App")
    st.write("Enter the text of the news article below:")

    # Text input for news article
    news_text = st.text_area("News Article Text", "")

    if st.button("Predict"):
        if news_text:
            # Preprocess the text (e.g., remove punctuation, tokenize)
            # ... Add your preprocessing code here ...
            
            # Make the prediction
            prediction = model.predict([news_text])[0]
            
            # Display the prediction
            if prediction == 0:
                st.write("The news article is predicted to be fake.")
            else:
                st.write("The news article is predicted to be genuine.")
        else:
            st.write("Please enter a news article.")

# Run the app
if __name__ == "__main__":
    main()

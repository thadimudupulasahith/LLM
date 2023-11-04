# Import necessary libraries
import torch  # PyTorch library
from transformers import pipeline  # Hugging Face Transformers library for NLP tasks

# Create a sentiment analysis pipeline using Hugging Face Transformers
sentiment_analyzer = pipeline('sentiment-analysis')

# Import the Streamlit library for creating web applications
import streamlit as st

# Define the main function for the Streamlit app
def main():
    # Set the title of the Streamlit web app
    st.title("Sentiment Analysis App")
    
    # Create a text input field for the user to enter text for sentiment analysis
    user_input = st.text_input("Enter a text for sentiment analysis:")
    
    # Check if the user has entered any text
    if user_input:
        # Analyze the sentiment of the user's input using the sentiment_analyzer pipeline
        result = sentiment_analyzer(user_input)
        sentiment = result[0]['label']  # Get the sentiment label (e.g., 'POSITIVE', 'NEGATIVE')
        score = result[0]['score']      # Get the sentiment score
        
        # Display the sentiment and score on the Streamlit web app
        st.write("Sentiment:", sentiment)
        st.write("Score:", score)

# Run the main function if the script is executed as the main program
if __name__ == "__main__":
    main()

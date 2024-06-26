import streamlit as st
import pandas as pd
import pickle
import tensorflow as tf
from tensorflow.keras.layers import Dense, Concatenate, Input, Dropout
from tensorflow.keras.models import load_model, Sequential, Model


def user_input():

    txt = st.text_area('Text to analyze', '''
    It was the best of times, it was the worst of times, it was
    the age of wisdom, it was the age of foolishness, it was
    the epoch of belief, it was the epoch of incredulity, it
    was the season of Light, it was the season of Darkness, it
    was the spring of hope, it was the winter of despair, (
    ''')
    
    
    data = {
        'Content': txt
        
    }
    features = pd.DataFrame(data, index=[0])
    return features

def app():
    st.title('Hate Speech Sentiment Analysis')
    # Getting user input
    input_df = user_input()

    # load model
    model_1 = load_model('model_lstm_3.keras')

    # Predict Score
    if st.button('Analyze Now'):
        predict_proba = model_1.predict(input_df)
        predictions = tf.where(predict_proba >= 0.5, 1, 0)
        if predictions == 1:
            st.write("Analysis: Hate Speech")
        else:
            st.write("Analysis: Non-Hate Speech")
    else:
        st.write('Analysis:')
    

app()
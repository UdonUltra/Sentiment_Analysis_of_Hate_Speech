import streamlit as st
import pandas as pd
# import joblib as jb
import eda
import prediction


#header
"""
# Graded Challenge 7
**Name    : Frederick Kurniawan Putra**

**Batch   : HCK016**

This is model deployment of Hate Speech Sentiment Prediction.
"""



PAGES = {
    "Eda": eda,
    "Prediction": prediction
}
st.sidebar.title('Navigation')
selection = st.sidebar.radio("Go to", list(PAGES.keys()))
page = PAGES[selection]
page.app()
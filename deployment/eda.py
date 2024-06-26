import streamlit as st
from PIL import Image

def app():
    st.title('EDA')
    
    # EDA 1
    st.write('1. Percentage of Hate Speech and Non Hate Speech')
    image = Image.open('eda_1.png')
    st.image(image)
    st.write('Here we can see that our dataset has 85.58% Non Hate Speech, while hate speech represents 14.42% data. This means that the data is imbalanced.')

    # EDA 2
    st.write('2. Most Frequent Unigram in dataset')
    image = Image.open('eda_2.png')
    st.image(image)
    st.write("In this data we can see that Most frequent Unigrams that might represent mockery and racism are white, black, slut, afro, faggot. This indicates that racism slur is a indication of hate speech.")
    
    # EDA 3
    st.write('3. Most Frequent Bigram in dataset')
    image = Image.open('eda_3.png')
    st.image(image)
    st.write("Here we can see that Most Frequent Bigrams in hate speech content also dominated with racial slur such as afro american, ching chong, non whites, while also followed by mockery such as shithole countries and fucking retard.")

    # EDA 4
    st.write('4. Top County that become topic of target in Content')
    image = Image.open('eda_4.png')
    st.image(image)
    st.write("Here we can see that country that become a topic or target for hate speeech are africa, america, europt or london. We can safely assume based on bigram analysis that the context is refering to african american.")

import streamlit as st

col1, col2, col3 = st.columns(3)

with col1:
    st.header('Google')
    st.image('image.jpg', width=200) 
    st.link_button('Go to Google', 'https://www.google.com')
with col2:
    st.header('Facebook')
    st.image('image2.jpg', width=200)
    st.link_button('Go to Facebook', 'https://www.facebook.com')
with col3:
    st.header('Twitter')
    st.image('image3.jpg', width=200)
    st.link_button('Go to Twitter', 'https://www.twitter.com')
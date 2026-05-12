import streamlit as st

st.title('Choose multiple companies')

list = st.multiselect('choose one or more companies',[
    'Tesla', 'Google', 'Microsoft', 'Apple', 'Intel'
    ], ['Google'])

st.write(list)
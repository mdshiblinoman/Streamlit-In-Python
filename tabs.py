import streamlit as st

tab1, tab2, tab3, tab4 = st.tabs(['Text Input', 'Time Input', 'Radio Button', 'Slider'])

with tab1:
    st.text_input("Enter some text:")

with tab2:
    st.time_input("Select a time:")

with tab3:
    st.radio("Choose an option:", ["Option 1", "Option 2", "Option 3"])

with tab4:
    st.slider("Select a value:", 0, 100, 50)
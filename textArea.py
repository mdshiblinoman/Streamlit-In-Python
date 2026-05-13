import streamlit as st

list = []

text = st.text_area(
    'Enter any text',
    '', placeholder='any text',
    max_chars=2000
)

button = st.button('Analyze')

if button:
    text_spilt = text.split(sep=" ")
    for word in text_spilt:
        list.append(word)
    st.write(f'your worth {len(text)} characters is {len(list)}')
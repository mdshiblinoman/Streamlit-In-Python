import streamlit as st

st.title('Create Sidebar:')

with st.sidebar:
    add_selectbox = st.selectbox(
        "What is your favorite color?",
        ("Blue", "Red", "Green")
    )

    add_input = st.text_input("What is your name?")
    add_radio = st.radio("What is your gender?", ("Male", "Female", "Other"))
    add_checkbox = st.checkbox("I agree to the terms and conditions")
    add_button = st.button("Submit")

if add_button:
    st.write(f'Your name is {add_input}, your favorite color is {add_selectbox}, your gender is {add_radio}, and you have {"agreed" if add_checkbox else "not agreed"} to the terms and conditions.')
import streamlit as st

car_type = ['toyota', 'BMW', 'ford', 'ferary']

car = st.text_input('Enter a car')

button = st.button('Submit')

if button == True:
    have_it = car.lower() in car_type

    if have_it:
        st.write('We have that car!')
    else:
        st.write('We do not have that car!')
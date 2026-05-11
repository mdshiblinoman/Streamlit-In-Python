# importing necessary libraries
import streamlit as st

# list of car types available
car_type = ['toyota', 'BMW', 'ford', 'ferary']

# input field to get the name of the car from the user
car = st.text_input('Enter a car')

# creating a button to submit the input
button = st.button('Submit')

# checking if the button is clicked and if the car is available in the list
if button == True:
    have_it = car.lower() in car_type       # checking if the car is available in the list and storing the result in have_it variable

# displaying the result based on the value of have_it variable
    if have_it:
        st.write('We have that car!')
    else:
        st.write('We do not have that car!')
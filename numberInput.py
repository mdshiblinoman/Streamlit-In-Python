import streamlit as st

num1 = st.number_input('Enter The First Number')
num2 = st.number_input('Enter the Second Number')

col = st.columns(4)

with col[0]:
    add = st.button('Add +')
with col[1]:
    sub = st.button('Sub -')
with col[2]:
    mult = st.button('Mult *')
with col[3]:
    div = st.button('Div /')

if add:
    st.write(f'Result is {num1 + num2}')
if sub:
    st.write(f'Result is {num1 - num2}')
if mult:
    st.write(f'Result is {num1 * num2}')
if div:
    st.write(f'Result is {num1 / num2}')

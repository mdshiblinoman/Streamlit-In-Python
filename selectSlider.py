import streamlit as st

st.title('Calculate Interest Rate')

amount = st.select_slider(
    'Select Amount',
    options=[1, 1000, 2000, 3000, 4000, 50000, 6000, 7000]
)

month = st.select_slider(
    'Select Month',
    options=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
)

st.subheader("Interest Rate")
st.text('2%')

cal = (amount / 100) * (1 / 365) * (month * 30)
st.write('Your PayBack is',int(cal))
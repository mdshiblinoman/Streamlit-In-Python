import streamlit as st

tab1, tab2, tab3 = st.tabs(['Text Input', 'Radio Button', 'Slider'])

with tab1:
    text = st.text_input("Enter some text:")
    st.write('text:', text)

    with st.expander('See explanation'):
        st.write('This is an example of an expander. You can put any content here, including text, images, or other Streamlit components.')

with tab2:
    option = st.radio("Choose an option:", ["Option 1", "Option 2", "Option 3"])
    st.write('option:', option)

    with st.expander('See explanation'):
        st.write('This is another expander. You can use it to hide or show additional information based on user interaction.')

with tab3:
    value = st.slider("Select a value:", 0, 100, 50)
    st.write('value:', value)

    with st.expander('See explanation'):
        st.write('This expander can be used to provide more details about the slider or to show related content when the user interacts with the slider.')
 

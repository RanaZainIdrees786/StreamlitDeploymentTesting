import streamlit as st

st.title("Hello Welcome to Streamlit")
st.write('this is a demo app to test streamlit deployment')
userinput = st.input_text("Hi how are you")

st.write(userinput)
st.write("Thank you for your response")
st.write("Have a great day")
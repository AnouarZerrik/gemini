import google.generativeai as genai
import streamlit as st


genai.configure(api_key='AIzaSyBLdPt9xCo9Ia1vpBuxfCl9EMq0FqXByyI')

st.title("Gemini AI :robot_face:")

st.write("Please enter a prompt below, and the model will generate a response.")
query =  st.text_input("")
prompt = st.button("Generate")
if prompt:
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(query)
    st.write("Response:")
    st.info(response.text)
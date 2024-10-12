from dotenv import load_dotenv
load_dotenv()
import os
import google.generativeai as genai
import streamlit as st
from PIL import Image

genai.configure(api_key=os.getenv("API_KEY"))

model = genai.GenerativeModel("gemini-1.5-flash")
def get_res(input,image):
    if input!="":
        response = model.generate_content([input,image])
        return response.text
    
st.set_page_config(page_title="Gen AI")

st.header("Gen AI Application")
input =st.text_input("Input Prompt",key="input")
upload_img = st.file_uploader("Choose a Image..",type=["jpg","png","jpeg"])
image = ""
if upload_img is not None:
    image = Image.open(upload_img)
    st.image(image,caption="Uploaded Image")

submit = st.button("Generate Response from prompt")

if submit:
    response = get_res(input,image)
    st.subheader("Response")
    st.write(response)
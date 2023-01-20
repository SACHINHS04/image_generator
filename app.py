import streamlit as st
import openai

st.title("Image Generator using OpenAI")
api_key = st.text_input("Enter your OpenAI API key")
prompt = st.text_input("Enter a prompt to generate an image")

if st.button("Generate"):
    if not api_key:
        st.error("API key is required")
    else:
        # Use the OpenAI API to generate an image
        response = openai.Image.create(
            prompt=prompt,
            api_key=api_key
        )
        image_url = response['data'][0]['url']
        st.image(image_url)
        file_name = prompt.replace(" ", "_") + ".jpg"
        st.file_downloader(file_name, caption='Download the image', download_url=image_url)

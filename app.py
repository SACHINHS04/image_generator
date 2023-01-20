import streamlit as st
import openai
import urllib.request

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
#         if st.button("Download"):
#             file_name = st.text_input("Enter the name of the file", value=prompt.replace(" ", "_") + ".jpg")
#             file_path = st.filesavebox("Select the location to save the file",default=file_name)
#         if file_path:
#             urllib.request.urlretrieve(image_url, file_path)
#             st.success("Image saved as {}".format(file_path))



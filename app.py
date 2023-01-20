import openai
import streamlit as st

st.title("Image Generator using OpenAI")

# Ask the user to input their OpenAI API key
api_key = st.text_input("Enter your OpenAI API key:")
openai.api_key = api_key

models = openai.Model.list()
model_options = [model.id for model in models['data']]
model_id = st.selectbox("Select the model", model_options)

def generate_image():
    prompt = st.text_input("Enter a prompt for the image:")

    completions = openai.Completion.create(
        engine=model_id,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    image_url = completions.choices[0].url
    st.image(image_url, width=300)
    st.markdown("[Download image]({})".format(image_url))

if st.button("Generate Image"):
    generate_image()

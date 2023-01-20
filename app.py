import openai
import streamlit as st

st.title("Image Generator using OpenAI")

# Ask the user to input their OpenAI API key
api_key = st.text_input("Enter your OpenAI API key:")
openai.api_key = api_key

models = openai.Model.list()
print(models)


def generate_image():
    prompt = st.text_input("Enter a prompt for the image:")
    with st.spinner("Waiting for the image to generate..."):
        completions = openai.Completion.create(
            engine=model_id,
            prompt=prompt,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.5,
        )
    try:
        image_url = completions.choices[0].url
        st.image(image_url, width=300)
        try:
            st.markdown("[Download image]({})".format(image_url))
        except Exception as e:
            st.error("Error occured, please check the image url or internet connection")
    except KeyError:
        st.error("Error occured, please check your prompt or the model you've selected")

if st.button("Generate Image"):
    generate_image()

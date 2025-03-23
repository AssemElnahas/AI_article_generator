import streamlit as st
from transformers import pipeline


def generate_article(prompt, max_length=500):
    generator = pipeline("text-generation", model="gpt2")
    article = generator(prompt, max_length=max_length, num_return_sequences=1)
    return article[0]['generated_text']


st.title("AI Article Generator")

prompt = st.text_input("Enter a topic for the article:")
if st.button("Generate Article"):
    if prompt:
        article = generate_article(prompt)
        st.subheader("Generated Article:")
        st.write(article)
    else:
        st.warning("Please enter a topic before generating an article.")

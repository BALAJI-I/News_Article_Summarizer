from dotenv import load_dotenv
import os
import streamlit as st

load_dotenv() #env variable will be created

GROQ_API_KEY = os.getenv('GROQ_API_KEY')

from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate

# Define prompt
prompt_template = """You are a journalist tasked with creating a short and catchy news article. Please read the provided article carefully. Summarize the key points, focusing on the most important information. Write in a clear and engaging style that is easy to understand. Keep the article concise, using simple and attractive language. Your article should have a compelling headline and a brief introduction that captures the reader's attention. Use bullet points for key facts if necessary.

Provided Article:
{text}
NEWS ARTICLE:"""
prompt = PromptTemplate.from_template(prompt_template)

model = ChatGroq(
    temperature=0,
    model="llama3-70b-8192",
)
article = """<YOUR ARTICLE>"""

chain = prompt | model

def summerise_article(article):
    return chain.invoke({"text": article}).content

st.title('News Article Summarizer')

uploaded_file = st.file_uploader("Upload your news article in .txt format", type="txt")

if uploaded_file is not None:
    file_content = uploaded_file.read().decode("utf-8")

    st.text_area("Your News Article", file_content, height=200)

    if st.button("Summarize Article"):
    
        sum_article = summerise_article(file_content)
        st.text_area("Summarised News Article", sum_article, height=400)
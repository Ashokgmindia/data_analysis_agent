import pandas as pd
import sqlite3
import streamlit as st
from pandasai import SmartDataframe
# from langchain_community.llms import Ollama
from langchain_groq.chat_models import ChatGroq
import os

llm = ChatGroq(model_name="llama3-8b-8192",
               api_key="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")

st.title("Chat with Data")

# File uploader for Excel or CSV file
uploaded_file = st.file_uploader(
    "Upload your Excel or CSV file", type=["xlsx", "csv"])

if uploaded_file is not None:
    if uploaded_file.name.endswith(".xlsx"):
        df = pd.read_excel(uploaded_file)
    else:
        df = pd.read_csv(uploaded_file)
    st.write("Data Preview:")
    st.dataframe(df)

    df = SmartDataframe(df, config={"llm": llm})

    question = st.text_input("Ask a question about your data:")

    if st.button("Submit"):
        if question:
            response = df.chat(question)
            st.write("Response:")
            st.write(response)
        else:
            st.write("Please enter a question.")

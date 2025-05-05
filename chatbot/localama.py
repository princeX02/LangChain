from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama
import streamlit as st
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Set Langchain environment variables
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")

# Prompt Template with instructions to return plain text only
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant. Respond to user queries in plain English, without using structured data like JSON or XML."),
        ("user", "Question: {question}")
    ]
)

# Streamlit app setup
st.title('Langchain Demo With LLAMA2 API')
input_text = st.text_input("Search the topic you want")

# Ollama LLaMA2 LLM setup
llm = Ollama(model="llama2")
output_parser = StrOutputParser()

# LangChain chain definition
chain = prompt | llm | output_parser

# Run chain if user input is provided
if input_text:
    result = chain.invoke({"question": input_text})
    st.write("Response:")
    st.write(result)

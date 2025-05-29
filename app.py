import os 
from dotenv import load_dotenv
load_dotenv()
from langchain_community.llms import Ollama
#os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")
#os.environ["LANGCHAIN_TRACING_V2"]="true"
#os.environ["LANGCHAIN_PROJECT"]=os.getenv("LANGCHAIN_PROJECT")
import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

prompt=ChatPromptTemplate.from_messages(
      [
          ("system","you are a helpful assistant. Please response to the question asked"),
          ("user", "Question:{question}")
      ]

)

st.title("Langchain Demo with Gemma model")
input_text=st.text_input("what question you have in mind")

llm=Ollama(model ="gemma:2b")
output_parser=StrOutputParser()
chain=prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({"question":input_text}))
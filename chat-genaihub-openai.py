# from langchain_openai import ChatOpenAI
from gen_ai_hub.proxy.langchain.openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser



import streamlit as st
import os
from dotenv import load_dotenv
load_dotenv()

# os.environ["OPENAI_API_KEY"]=os.getenv("OPENAI_API_KEY")
## Langmith tracking
os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")

os.environ["AICORE_AUTH_URL"] = os.getenv("AICORE_AUTH_URL")
os.environ["AICORE_CLIENT_ID"] = os.getenv("AICORE_CLIENT_ID")
os.environ["AICORE_CLIENT_SECRET"] = os.getenv("AICORE_CLIENT_SECRET")
os.environ["AICORE_RESOURCE_GROUP"] = os.getenv("AICORE_RESOURCE_GROUP")
os.environ["AICORE_BASE_URL"] = os.getenv("AICORE_BASE_URL")



# prompt=ChatPromptTemplate.from_messages(
#     [
#         ("system","You are a Experienced SAP BTP CAPM (Nodejs) CDS Developer. Please response to the BTP technical related question only"),
#         ("user","Question:{question}")
#     ]
# )

prompt=ChatPromptTemplate.from_messages(
    [
        ("system","You are a Experienced SAP ABAP Developer. Please response to the ABAP technical related question only"),
        ("user","Question:{question}")
    ]
)


# streamlit framework

st.title('Langchain With Gen Ai Hub - OPENAI')
input_text=st.text_input("You can ask anything")
# give me a sample project structure


LLM_DEPLOYMENT_ID = os.getenv("LLM_DEPLOYMENT_ID")

# openAI LLm 
llm=ChatOpenAI(deployment_id=LLM_DEPLOYMENT_ID)
output_parser=StrOutputParser()
chain=prompt|llm|output_parser


if input_text:
    st.write(chain.invoke({'question':input_text}))
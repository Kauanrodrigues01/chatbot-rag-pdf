import os
import streamlit as st
from app.settings import OPENAI_API_KEY

os.environ['OPENAI_API_KEY'] = OPENAI_API_KEY

st.set_page_config(
    page_title='Chatbot',
    page_icon='🤖',
)

st.header('🤖 Chat com seus documentos (RAG)')

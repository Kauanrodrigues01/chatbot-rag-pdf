import os

import streamlit as st

from app.settings import OPENAI_API_KEY
from rag.loader import process_pdf_for_chunks
from rag.rag_chain import ask_question
from rag.vector_store import add_documents_to_vector_store, load_vector_store

os.environ['OPENAI_API_KEY'] = OPENAI_API_KEY

st.set_page_config(
    page_title='Chatbot',
    page_icon='🤖',
)

st.header('🤖 Chat com seus documentos (RAG)')

vector_store = load_vector_store()

with st.sidebar:
    st.header('Upload de arquivos 📄')

    upload_files = st.file_uploader(
        label='Faça o upload de arquivos PDF',
        type=['pdf'],
        accept_multiple_files=True,
    )

    send_button = st.button('Enviar')

    if send_button:
        if upload_files:
            chunks = []

            for file in upload_files:
                file_chunks = process_pdf_for_chunks(file=file)
                chunks.extend(file_chunks)

            vector_store = add_documents_to_vector_store(chunks)
        else:
            st.warning('Nenhum arquivo foi enviado.')

    model_options = [
        'gpt-3.5-turbo',
        'gpt-4',
        'gpt-4-turbo',
        'gpt-4o-mini',
        'gpt-4o',
    ]
    selected_model = st.sidebar.selectbox(
        label='Selecione o modelo LLM',
        options=model_options,
    )

if 'history_messages' not in st.session_state:
    st.session_state['history_messages'] = []

question = st.chat_input('Como posso ajudar?')

if vector_store and question:
    for message in st.session_state['history_messages']:
        st.chat_message(message.get('role')).write(message.get('content'))

    st.chat_message('user').write(question)
    st.session_state['history_messages'].append({'role': 'user', 'content': question})

    with st.spinner('Buscando resposta...'):
        response = ask_question(
            model=selected_model,
            vector_store=vector_store,
            query=question,
            history_messages=st.session_state['history_messages']
        )

        st.chat_message('ai').write(response)
        st.session_state['history_messages'].append({'role': 'ai', 'content': response})

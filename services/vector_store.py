from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings

from app.settings import PERSIST_DIRECTORY

def load_vector_store():
    try:
        vector_store = Chroma(
            persist_directory=PERSIST_DIRECTORY,
            embedding_function=OpenAIEmbeddings(),
        )
        return vector_store
    except Exception as e:
        print(f'Erro ao recuperar a Vector Store: {e}')
        return None
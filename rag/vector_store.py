from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings

from app.settings import PERSIST_DIRECTORY

_vector_store_instance = None


def load_vector_store():
    global _vector_store_instance

    if _vector_store_instance is not None:
        return _vector_store_instance

    try:
        _vector_store_instance = Chroma(
            persist_directory=PERSIST_DIRECTORY,
            embedding_function=OpenAIEmbeddings(),
        )
        return _vector_store_instance
    except Exception as e:
        print(f'Erro ao recuperar a Vector Store: {e}')
        return None


def add_documents_to_vector_store(chunks):
    vector_store = load_vector_store()
    vector_store.add_documents(chunks)
    return vector_store

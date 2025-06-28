import os
import tempfile

from langchain_community.document_loaders import PyPDFLoader

from rag.splitter import split_documents


def process_pdf_for_chunks(file):
    with tempfile.NamedTemporaryFile(delete=False, suffix='.pdf') as temp_file:
        temp_file.write(file.read())
        temp_file_path = temp_file.name

    loader = PyPDFLoader(temp_file_path)
    docs = loader.load()

    os.remove(temp_file_path)

    chunks = split_documents(docs=docs)

    return chunks

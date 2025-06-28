from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains.retrieval import create_retrieval_chain
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate, HumanMessagePromptTemplate, SystemMessagePromptTemplate

def ask_question(model: str, vector_store, query: str):
    retriever = vector_store.as_retriever()
    llm = ChatOpenAI(
        model=model
    )
    
    system_prompt = '''
    Use o contexto para responder as perguntas.
    Se não souber, diga que não há informações suficientes para responder a pergunta.
    Responda em markdown com visualizações elaboradas.
    Contexto: {context}
    '''
    
    prompt = ChatPromptTemplate.from_messages(
        [
            SystemMessagePromptTemplate.from_template(system_prompt),
            HumanMessagePromptTemplate.from_template('{input}')
        ]
    )
    
    # Esta função cria um chain que recebe uma lista de documentos (List[Document]) e:
    # - Concatena o conteúdo dos documentos em uma única string e insere na variável "context" do prompt.
    # - Substitui a variável "input" pela pergunta do usuário (passada como argumento).
    # - Passa o prompt final para o LLM gerar uma resposta baseada no contexto e na pergunta.
    # Obs: o nome "context" é o valor padrão de document_variable_name usado internamente pelo chain.
    combine_docs_chain = create_stuff_documents_chain(
        llm=llm,
        prompt=prompt
    )

    # Esta função cria um chain completo de RAG (Retrieval-Augmented Generation) que:
    # - Recebe uma pergunta (input do usuário).
    # - Usa o retriever (baseado em vetor, como Chroma) para buscar os documentos mais relevantes com base nessa pergunta.
    # - Passa os documentos encontrados para o question_answer_chain (criado com create_stuff_documents_chain), que concatena os textos e injeta no prompt junto com a pergunta.
    # - O LLM então gera uma resposta com base nos documentos encontrados.
    # Resultado final: uma cadeia que encapsula tanto a recuperação quanto a geração de resposta com base no contexto.
    # Obs: o input esperado é um dicionário com a chave "input", e a saída é um dicionário com a chave "answer".
    chain = create_retrieval_chain(
        retriever=retriever,
        combine_docs_chain=combine_docs_chain,
    )

    response = chain.invoke({'input': query})
    return response.get('answer')


    # Fluxo completo da cadeia de RAG usando retrieval_chain + combine_docs_chain:
    #
    # 1. O retrieval_chain recebe um dicionário com a chave "input" (valor padrão do input_key) contendo a pergunta do usuário.
    # 2. Esse valor de "input" é usado pelo retriever para consultar a vector store (ex: Chroma) e retornar os documentos relevantes (List[Document]).
    # 3. Os documentos encontrados são passados automaticamente pelo retrieval_chain para o combine_docs_chain (criado via create_stuff_documents_chain).
    # 4. O combine_docs_chain:
    #    - Extrai o conteúdo dos documentos e concatena tudo em uma única string, substituindo no prompt a variável "context" (ou o nome definido em document_variable_name).
    #    - Insere também o valor de "input" (a pergunta) na variável correspondente no prompt (neste caso, "{input}").
    #    - Com o prompt completo (contexto + pergunta), o LLM é invocado para gerar uma resposta.
    # 5. A resposta gerada pelo LLM é retornada pela retrieval_chain em um dicionário com a chave "answer" (valor padrão do output_key).
    #
    # Resultado: uma cadeia que abstrai tanto a recuperação de contexto quanto a geração de resposta contextualizada.

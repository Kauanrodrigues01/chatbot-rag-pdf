# 🤖 Chat com Documentos PDF usando RAG (Retrieval-Augmented Generation)

<p align="center">
  <img src="https://raw.githubusercontent.com/Kauanrodrigues01/Kauanrodrigues01/refs/heads/main/images/projetos/chatbot-com-ia/page.png" width="70%">
</p>

Este projeto é um chatbot construído com **Streamlit** e **LangChain**, que utiliza a técnica de **RAG (Retrieval-Augmented Generation)** para responder perguntas baseadas em arquivos PDF enviados pelo usuário.

A aplicação permite:

* Upload de arquivos PDF via interface web.
* Processamento e chunking dos documentos.
* Indexação dos chunks em uma base vetorial persistente.
* Consulta semântica com modelos da OpenAI (gpt-3.5, gpt-4, gpt-4o, etc).
* Exibição de respostas com contexto, utilizando markdown.

---

## 📁 Estrutura do Projeto

```
.
├── app/
│   ├── settings.py            # Váriaveis de Ambiente
│
├── rag/
│   ├── __init__.py
│   ├── loader.py              # Carregamento e leitura de PDFs
│   ├── rag_chain.py           # Implementação do RAG (retrieval + generation)
│   ├── splitter.py            # Divisão de documentos em chunks
│   ├── vector_store.py        # Vetorização e persistência com ChromaDB
│   └── settings.py            # Configurações (API key e diretório)
|
├── main.py                    # Interface principal com Streamlit
```

---

## 🚀 Tecnologias Utilizadas

* **[Python](https://www.python.org/)** – Linguagem de programação principal utilizada no projeto.
* **[LangChain](https://www.langchain.com/)** – Framework para construção de aplicações de RAG (Retrieval-Augmented Generation).
* **[Streamlit](https://streamlit.io/)** – Biblioteca de Python para criação de interfaces web interativas de forma rápida.
* **[ChromaDB](https://www.trychroma.com/)** – Banco de dados vetorial local utilizado para armazenar embeddings de documentos.
* **[OpenAI API](https://platform.openai.com/)** – API de modelos de linguagem usados para gerar respostas baseadas no contexto recuperado.

---

## 🧠 Como Funciona

1. **Upload de PDFs**: O usuário envia arquivos pela interface.
2. **Processamento**:

   * PDFs são convertidos em texto.
   * Os textos são divididos em **chunks** com sobreposição.
3. **Vetorização**:

   * Os chunks são convertidos em vetores com `OpenAIEmbeddings`.
   * Os vetores são armazenados com persistência no ChromaDB.
4. **Consulta**:

   * O usuário envia uma pergunta.
   * A base vetorial é consultada para buscar os chunks mais relevantes.
   * Um modelo LLM é invocado com esses chunks como contexto.
5. **Resposta**:

   * A resposta do modelo é exibida no chat, com histórico salvo via `st.session_state`.

---

## 🧪 Modelos Suportados

* `gpt-3.5-turbo`
* `gpt-4`
* `gpt-4-turbo`
* `gpt-4o`
* `gpt-4o-mini`

O modelo é selecionado diretamente na barra lateral da interface.

---

## ⚙️ Configuração

### 1. Instalar dependências

```bash
pip install -r requirements.txt
```

> Certifique-se de que as bibliotecas como `streamlit`, `langchain`, `openai`, `chromadb`, `python-decouple` estejam listadas no seu `requirements.txt`.

---

### 2. Variáveis de ambiente

Crie um arquivo `.env` na raiz do projeto com:

```
OPENAI_API_KEY=sk-...
PERSIST_DIRECTORY=vector-db
```

---

### 3. Rodar o projeto

```bash
streamlit run app/main.py
```

---

## 🤩 Componentes Internos

| Arquivo           | Responsabilidade                                         |
| ----------------- | -------------------------------------------------------- |
| `main.py`         | Interface com o usuário e orquestração geral             |
| `rag_chain.py`    | Monta o RAG chain (retrieval + generation)               |
| `loader.py`       | Carrega PDFs como documentos LangChain                   |
| `splitter.py`     | Divide os documentos em chunks com sobreposição          |
| `vector_store.py` | Cria e gerencia o repositório vetorial persistente       |
| `settings.py`     | Define a API key da OpenAI e o diretório de persistência |

---

## 📀 Exemplos de Uso

1. Envie um ou mais arquivos PDF.
2. Faça perguntas como:

   * “Qual é o objetivo principal do contrato?”
   * “O que diz a cláusula de rescisão?”
3. A IA irá buscar os trechos mais relevantes e responder com base no conteúdo.

---

## 🛡️ Segurança

* Nenhum dado é enviado ou armazenado remotamente (a não ser via OpenAI API).
* O uso de arquivos locais e ChromaDB com persistência evita dependência de infraestrutura externa.

---

## 🧼 Boas práticas aplicadas

* Código organizado em módulos separados por responsabilidade.
* Uso de variáveis de ambiente com fallback e validação.
* Compliant com **PEP8** e **Ruff**.
* Histórico de mensagens gerenciado por sessão.
* Validação de arquivos e mensagens no frontend.

---

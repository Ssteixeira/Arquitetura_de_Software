import os

# LangChain
from langchain.embeddings import SentenceTransformerEmbeddings
from langchain.vectorstores import FAISS
from langchain.docstore.document import Document
from langchain.chains import RetrievalQA
from langchain.llms import HuggingFacePipeline

# Transformers
from transformers import pipeline

# -----------------------------------------------------------------------------
# 1. Configuração do modelo LLM local (text-generation)
# -----------------------------------------------------------------------------
def carregar_llm_local():
    gerador = pipeline(
        "text-generation",
        model="distilgpt2",
        max_new_tokens=50,
        do_sample=True,
        temperature=0.7
    )
    return HuggingFacePipeline(pipeline=gerador)

# -----------------------------------------------------------------------------
# 2. Criação de documentos de exemplo
# -----------------------------------------------------------------------------
def dividir_texto(texto, tamanho_chunk=200):
    texto_limpo = " ".join(texto.split())
    return [texto_limpo[i:i + tamanho_chunk] for i in range(0, len(texto_limpo), tamanho_chunk)]

def carregar_documentos():
    textos = [
        """Arquitetura em Camadas (Layered Architecture) é um estilo de arquitetura de software 
        onde as responsabilidades são organizadas em camadas...""",
        """A Arquitetura de Microsserviços incentiva a criação de vários serviços pequenos e 
        independentes...""",
        """Um Monólito é um estilo de arquitetura onde todo o código e responsabilidades 
        ficam unificados em uma única base...""",
        """Domain-Driven Design (DDD) enfatiza a modelagem do domínio de negócio..."""
    ]

    docs = []
    for i, txt in enumerate(textos, start=1):
        for pedaco in dividir_texto(txt, 150):
            docs.append(Document(page_content=pedaco, metadata={"fonte": f"doc_{i}"}))
    return docs

# -----------------------------------------------------------------------------
# 3. Construção do índice vetorial FAISS com embeddings
# -----------------------------------------------------------------------------
def construir_index(docs):
    embeddings = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")
    return FAISS.from_documents(docs, embeddings)

# -----------------------------------------------------------------------------
# 4. Construção da cadeia de Pergunta e Resposta
# -----------------------------------------------------------------------------
def criar_qa_chain(llm, index):
    return RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=index.as_retriever()
    )

# -----------------------------------------------------------------------------
# 5. Execução das perguntas
# -----------------------------------------------------------------------------
def rodar_perguntas(qa_chain):
    perguntas = [
        "O que é uma arquitetura em camadas e que camadas ela normalmente possui?",
        "Quais são os benefícios de uma arquitetura de microsserviços?",
        "Explique as vantagens de ter uma arquitetura monolítica.",
        "O que é Domain-Driven Design (DDD) e por que ele é útil?"
    ]
    for i, pergunta in enumerate(perguntas, start=1):
        print(f"\n=== Pergunta {i}: {pergunta}")
        resposta = qa_chain.run(pergunta)
        print("Resposta:", resposta)

# -----------------------------------------------------------------------------
# Função principal
# -----------------------------------------------------------------------------
def main():
    print("🚀 Carregando modelo...")
    llm = carregar_llm_local()

    print("📄 Carregando documentos...")
    docs = carregar_documentos()

    print("📦 Criando índice vetorial...")
    index = construir_index(docs)

    print("🧠 Criando cadeia de perguntas e respostas...")
    qa_chain = criar_qa_chain(llm, index)

    print("❓ Respondendo perguntas...")
    rodar_perguntas(qa_chain)

if __name__ == "__main__":
    main()

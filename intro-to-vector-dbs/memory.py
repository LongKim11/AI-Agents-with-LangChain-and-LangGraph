import os 
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import CharacterTextSplitter
from langchain_openai import OpenAIEmbeddings, OpenAI
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import PromptTemplate
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains.retrieval import create_retrieval_chain
from langchain import hub
from dotenv import load_dotenv

load_dotenv()

if __name__ == "__main__":
    print("FAISS Vector Store...")

    loader = PyPDFLoader("example.pdf")

    documents = loader.load()

    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=30, separator="\n")

    docs = text_splitter.split_documents(documents)

    embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
    
    vectorstore = FAISS.from_documents(docs, embeddings)

    vectorstore.save_local("faiss_index_usenix")

    new_vectorstore = FAISS.load_local("faiss_index_usenix", embeddings, allow_dangerous_deserialization=True)

    retrieval_qa_chat_prompt = hub.pull("langchain-ai/retrieval-qa-chat")

    combine_docs_chain = create_stuff_documents_chain(OpenAI(model="gpt-4o-mini"), retrieval_qa_chat_prompt)

    retrieval_chain = create_retrieval_chain(retriever=new_vectorstore.as_retriever(), combine_docs_chain=combine_docs_chain)

    result = retrieval_chain.invoke(input={"input": "What is the main topic of the document?"})

    print(result["answer"])
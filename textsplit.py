import nltk
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import NLTKTextSplitter

def load_and_split_pdf:

    loader = PyPDFLoader("/content/lyft_2021.pdf")
    pages = loader.load_and_split()
    nltk.download('punkt')
    nltk_splitter = NLTKTextSplitter(chunk_size=1000)

    chunks=[]

    for p in pages:
        texts = nltk_splitter.split_text(p.page_content)
        chunks.extend(texts)

    return chunks

from textsplit import load_and_split_pdf
from openai_utils import generate_embedding, generate_summary
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import MongoDBAtlasVectorSearch
from pymongo import MongoClient
from langchain_community.vectorstores import MongoDBAtlasVectorSearch

DB_NAME = 'langchain_demo'
COLLECTION_NAME = 'emp-policy'
ATLAS_VECTOR_SEARCH_INDEX_NAME = "vector_index"


def create_connection():
    client = MongoClient(key_param.MONGO_URI)

    # Send a ping to confirm a successful connection
    try:
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
    except Exception as e:
        print(e)

    # Configure db details
    db = client[DB_NAME]
    return db[COLLECTION_NAME]



# Drive document ingestion
def ingest_documents(pdf_location):
    # Load chunks from the document
    chunks = load_and_split_pdf(pdf_location)

    summaries = [generate_summary(chunk) for chunk in chunks]
    embeddings_model = OpenAIEmbeddings(openai_api_key="", disallowed_special=())
    collection = create_connection()
    MongoDBAtlasVectorSearch.from_documents( 
                                documents=summaries, 
                                embedding= embeddings_model, 
                                collection=collection,
                                index_name=ATLAS_VECTOR_SEARCH_INDEX_NAME 
                                                    )


# Drive query processing
def process_query(query_text):
    vector_search = MongoDBAtlasVectorSearch.from_connection_string(
        "mongodb+srv://chunking_user:Hiq22idKv94I0YQN@cluster0.jqn2q4r.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0",
        DB_NAME + "." + COLLECTION_NAME,
        OpenAIEmbeddings(openai_api_key="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", disallowed_special=()),
        index_name=ATLAS_VECTOR_SEARCH_INDEX_NAME,
    )

    print("Fetch results")
    results = vector_search.similarity_search_with_score(
        query=query_text, k=5,
    )
    
    for result in results:
        print(result)

    # Need to construct prompt with original query and results
    # of vector search.


# ingest_documents('./data/lyft_2021.pdf')
        
process_query("What is the title of the document")
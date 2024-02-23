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
    

import chromadb
import google.generativeai as genai
from  Embeddata import  GeminiEmbeddingFunction
from typing import List
from Loadfilecsv import  getarray, load_csv,split_text
import os  
from  dotenv import  load_dotenv
def create_chroma_db(documents:List, path:str, name:str):
    """
    Creates a Chroma database using the provided documents, path, and collection name.

    Parameters:
    - documents: An iterable of documents to be added to the Chroma database.
    - path (str): The path where the Chroma database will be stored.
    - name (str): The name of the collection within the Chroma database.

    Returns:
    - Tuple[chromadb.Collection, str]: A tuple containing the created Chroma Collection and its name.
    """
    chroma_client = chromadb.PersistentClient(path=path)

    db = chroma_client.create_collection(name=name, embedding_function=GeminiEmbeddingFunction())

    for i, d in enumerate(documents):
        db.add(documents=d, ids=str(i))

    return db, name
def load_chroma_collection(path, name):
    """        print(i)
        print(d)
    Loads an existing Chroma collection from the specified path with the given name.

    Parameters:
    - path (str): The path where the Chroma database is stored.
    - name (str): The name of the collection within the Chroma database.

    Returns:
    - chromadb.Collection: The loaded Chroma Collection.
    """
    chroma_client = chromadb.PersistentClient(path=path)
    db = chroma_client.get_collection(name=name, embedding_function=GeminiEmbeddingFunction())

    return db
# value  =  load_csv('FAQ.csv')
# chunked_text = getarray(value)
# # db,name =create_chroma_db(documents=chunked_text, 
# #                           path="/home/anh/Downloads/testcsv/chroma_db", #replace with your path
# #                           name="rag_experiment_v2")
# h =load_chroma_collection(path="/home/anh/Downloads/testcsv/chroma_db",name="rag_experiment_v2")
# print(h)
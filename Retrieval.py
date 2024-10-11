import chromadb
import google.generativeai as genai
from  Embeddata import  GeminiEmbeddingFunction
from typing import List
from Loadfilecsv import  getarray, load_csv,split_text
import os  
from  dotenv import  load_dotenv
from  Storeembendding import load_chroma_collection
def get_relevant_passage(query, db, n_results):
  passage = db.query(query_texts=[query], n_results=n_results)['documents'][0]
  return passage # return list document  neighbor

# db = load_chroma_collection('/home/anh/Downloads/testcsv/chroma_db',name="rag_experiment_v2")
# passage = get_relevant_passage('Tôi có thể thực hiện đổi mã PIN ?',db=db,n_results=3)
# print(passage[1])
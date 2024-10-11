import chromadb
import google.generativeai as genai
from Embeddata import GeminiEmbeddingFunction
from typing import List
from Loadfilecsv import load_csv, split_text
import os  
from dotenv import load_dotenv
from Storeembendding import load_chroma_collection
from Retrieval import get_relevant_passage
from Generation import make_rag_prompt

def generate_answer_from_prompt(prompt):
    gemini_api_key = os.getenv("GOOGLE_API_KEY")
    if not gemini_api_key:
        raise ValueError("Gemini API Key not provided. Please provide GEMINI_API_KEY as an environment variable")
    genai.configure(api_key=gemini_api_key)
    model = genai.GenerativeModel('gemini-pro')
    answer = model.generate_content(prompt)
    return answer.text

def generate_answer(db, query):
    # retrieve top 3 relevant text chunks
    relevant_text = get_relevant_passage(query, db, n_results=3)
    prompt = make_rag_prompt(query,relevant_passage=relevant_text)  # joining the relevant chunks to create a single passage
    answer = generate_answer_from_prompt(prompt)  # Call the renamed function

    return answer

# Load the Chroma collection
db = load_chroma_collection(path="/home/anh/Downloads/testcsv/chroma_db",  # replace with path of your persistent directory
                            name="rag_experiment_v2")  # replace with the collection name

# Generate answer for the query
answer = generate_answer(db, query="làm sao để gia vị món canh thêm đậm đà?")
print(answer)

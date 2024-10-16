import chromadb
import google.generativeai as genai
from  Embeddata import  GeminiEmbeddingFunction
from typing import List
from Loadfilecsv import load_csv , split_text,split_text
import os  
from  dotenv import  load_dotenv
from Storeembendding import load_chroma_collection
from Retrieval import get_relevant_passage
import re
def make_rag_prompt(query, relevant_passage):
  if isinstance(relevant_passage, list) and len(relevant_passage) > 0:
        # Lấy đoạn văn bản đầu tiên từ danh sách
        relevant_passage = relevant_passage[0]  # Lấy đoạn văn đầu tiên
        a = [relevant_passage]
        escaped=re.split(r'\?\s*Answer:\s*', a[0])
        # print(escaped[1])
        

  prompt = ("""You are a helpful and informative bot that answers questions using text from the reference passage included below. \
  Be sure to respond in a complete sentence, being comprehensive, including all relevant background information. \
  However, you are talking to a non-technical audience, so be sure to break down complicated concepts and \
  strike a friendly and converstional tone. \
  If the passage is irrelevant to the answer, you may ignore it.
  QUESTION: '{query}'
  PASSAGE: '{relevant_passage}'

  ANSWER:
  """).format(query=query, relevant_passage=escaped[1])
#   print(prompt)
  return prompt
# Giả sử bạn đã có db từ hàm load_chroma_collection
# db = load_chroma_collection(path="/home/anh/rag/chroma_db", name="rag_experiment")

# # Giả sử bạn đã có một câu hỏi
# query = "What do Guatemalans do on the Day of the Dead?"

# # Lấy một đoạn văn liên quan
# relevant_passage = get_relevant_passage(query=query, db=db, n_results=1)  # Chỉ lấy 1 kết quả

# # Gọi hàm make_rag_prompt
# prompt = make_rag_prompt(query=query, relevant_passage=relevant_passage)

# In ra prompt
# print(prompt)
# make_rag_prompt('hello',relevant_passage=['Questions: Tôi nhập đúng mã PIN được cấp nhưng không rút được tiền, tôi cần xử lý thế nào? Answer: Quý khách vui lòng liên hệ tổng đài 1900545413 (đối với khách hàng thường)/18001565 (đối với KH ưu tiên) hoặc CN/PGD VCB gần nhất để được hỗ trợ'])
# a = ['Questions: Tôi nhập đúng mã PIN được cấp nhưng không rút được tiền, tôi cần xử lý thế nào? Answer: Quý khách vui lòng liên hệ tổng đài 1900545413 (đối với khách hàng thường)/18001565 (đối với KH ưu tiên) hoặc CN/PGD VCB gần nhất để được hỗ trợ']
# print(a[0])
# tach = re.split(r'\?\s*Answer:\s*', a[0])
# print(tach)
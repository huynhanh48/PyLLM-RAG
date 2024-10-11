import csv
import re
def  load_csv(filepath: str):
    with open(filepath, newline='',encoding='utf-8 ') as csvfile:
        reader = csv.DictReader(csvfile)
        return list(reader)
def split_text(text: str):
    # Tách văn bản dựa trên hai hoặc nhiều dấu xuống dòng liên tiếp (có thể kèm theo dấu cách)
    text = text.replace('\u200b', '')
    split_text = re.split(r'\n\s*\n', text)
    return [i.strip() for i in split_text if i.strip() != ""]  # Loại bỏ các khoảng trắng không cần thiết

# Ví dụ gọi hàm
def getarray(document: list):
    arraydict = []
    for i in document:
        Question = split_text(i['Question'])[0]
        Answer = split_text(i['Answer'])[0]
        arraydict.append('Questions: '+Question +' '+ 'Answer: '+Answer)  # Thay vì từ điển, lưu cặp Question và Answer dưới dạng list
    return [i.replace('\n','') for i in arraydict]

value  =  load_csv('FAQ.csv')
# arraydict = getarray(value)





 

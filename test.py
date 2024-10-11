import re 
import csv
import re
def  getdict(filepath: str):
    with open(filepath, newline='',encoding='utf-8 ') as csvfile:
        reader = csv.DictReader(csvfile)
        return list(reader)
#split_text = re.split(r'\n\s*\n', text)
# s = 'hhahahaha     toi da    lam bai tap    \n nolooorem  '
# s =  re.split(r'\n \s*',s)
# t=[i.strip() for i in s if i.strip() != ""] 
# print(s)
# print(t)
value  =  getdict('FAQ.csv')
print(value)
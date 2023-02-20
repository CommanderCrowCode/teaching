import re

with open('raw_thai.txt','r') as file:
    exam_raw = file.read()
   
answer_re = re.compile(r'^[ก,ข,ค,ง]\.\s+(.*)$')
answer_sub = re.compile(r'\\choice{\1}')

re.sub(answer_re,answer_sub,exam_raw)


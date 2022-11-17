# import httpx
#
# url_list = ['https://www.google.com', 'https://www.google.com/fgsag', 'https://google.com']
#
# for url in url_list:
#     res = httpx.get(url)
#     status = res.status_code
#     print(url, res, sep='.....')


import os
from dotenv import load_dotenv
load_dotenv()
import openai

openai.api_key = os.getenv('OPENAI_API_KEY')

def openai_ans(my_questions):
  response = openai.Completion.create(
    model="text-davinci-002",
    prompt=my_questions,
    temperature=0.7,
    max_tokens=321,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
  )
  data = response.get('choices')[0].get('text').strip('\n')
  return data

data = openai_ans('write 2 questinos about python')
number_list = ['1. ', '2. ', '3. ', '4. ', '5. ']

for number in number_list:
  data = data.replace(number, '')

questions = data.split('\n')

while '' in questions:
  questions.remove('')

questions_ans = {}
for q in questions:
  answer = openai_ans(q)
  questions_ans[q] = answer

print(questions_ans)

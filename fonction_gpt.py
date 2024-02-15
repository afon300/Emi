import openai
import os
    
def GPT(prompt):
  with open('key.txt', 'r') as f:
   key = f.read()
  openai.api_key = key
  completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo", 
    messages=[{"role": "user", "content": prompt}]
  )

  reponse = (completion['choices'][0]['message']['content'])
    
  return reponse
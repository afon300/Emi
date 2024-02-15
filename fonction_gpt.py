import openai
    
def GPT(prompt):
  openai.api_key = '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'

  completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo", 
    messages=[{"role": "user", "content": prompt}]
  )

  reponse = (completion['choices'][0]['message']['content'])
  
  return reponse
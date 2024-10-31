import os
from dotenv import load_dotenv
from openai import OpenAI
from datetime import datetime, timedelta
import pprint
load_dotenv()

openai = OpenAI(api_key=os.environ.get('OPEN_API_KEY'))

def get_ai_response(answers):
  prompt=f'''You are a life coach. Looking at the clients form that they filled out, can you give advice and systemic steps on how the client can achieve what they desire and then end of with motivational words. This can be about 300-400 words. Here is the form they filled out: {answers}.'''
  response = openai.chat.completions.create(
		model="gpt-4o",
    messages=[{
      'role': 'user',
      'content': prompt
    }],
		temperature=0.2,
		max_tokens=16384,
	)
  return response.choices[0].message.content
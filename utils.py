import os
from dotenv import load_dotenv
from openai import OpenAI
from datetime import datetime, timedelta
import pprint
load_dotenv()

openai = OpenAI(api_key=os.environ.get('OPEN_API_KEY'))

def get_ai_response(answers):
  prompt=f'''You are a life coach. Come up with a 300-400 word summary for the client. Here is the questionnaire they filled out: {answers}.'''
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
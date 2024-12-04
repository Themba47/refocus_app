import json
import pprint
from flask import Flask, render_template, request, jsonify
from typing import Union
from sqlstatement import get_data, insert_answers
from utils import get_ai_response, get_logo_ai_response

from fastapi import FastAPI

app = Flask(__name__)

def page_not_found(e):
  return render_template('404.html'), 404

app.register_error_handler(404, page_not_found)

@app.route("/", methods=["GET", "POST"])
def home():
   questions = get_data()
   
   if request.method == 'POST':
     answers = json.loads(request.data)
     email = answers.pop('user_email')
     insert_answers(email, json.dumps(answers))
     return jsonify({"result": get_ai_response(answers)})
     
   return render_template('index.html', questions=questions)
 
 
@app.route("/logomaker", methods=["GET", "POST"])
def logo_maker():
  
   if request.method == 'POST':
     answers = json.loads(request.data)
    #  email = answers.pop('user_email')
    #  insert_answers(email, json.dumps(answers))
     print("---------------------------")
     prompt = f"Create a {answers['Question_3']} style logo for a {answers['Question_2']} brand called '{answers['Question_1']}' that conveys a {answers['Question_6']} feel. Use {answers['Question_4']} and consider incorporating a {answers['Question_5']}. Avoid {answers['Question_7']}."
     return jsonify({"result": get_logo_ai_response(prompt)})
     
   return render_template('logomaker.html')
 
 
@app.route("/staysharp", methods=["GET", "POST"])
def staysharp():
  
   if request.method == 'POST':
     answers = json.loads(request.data)
    #  email = answers.pop('user_email')
    #  insert_answers(email, json.dumps(answers))
     print("---------------------------")
     prompt = f"Create a {answers['Question_3']} style logo for a {answers['Question_2']} brand called '{answers['Question_1']}' that conveys a {answers['Question_6']} feel. Use {answers['Question_4']} and consider incorporating a {answers['Question_5']}. Avoid {answers['Question_7']}."
     return jsonify({"result": get_logo_ai_response(prompt)})
     
   return render_template('staysharp.html')

 
if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8885', debug=True)
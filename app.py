from flask import Flask, render_template, request
from typing import Union
from sqlstatement import get_data

from fastapi import FastAPI

app = Flask(__name__)

def page_not_found(e):
  return render_template('404.html'), 404

app.register_error_handler(404, page_not_found)

@app.route("/", methods=["GET", "POST"])
def home():
   questions = get_data()
   # return render_template('index.html', **locals())
   return render_template('index.html', questions=questions)

 
# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port='8885', debug=True)
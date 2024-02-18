import os
from dotenv import load_dotenv
from flask import Flask, render_template, jsonify, request

from src.constants import prompt_file_path
from src.utils import read_prompt
from src.exception import CustException
from src.logger import logging
from src.chatmodel import Model

app = Flask(__name__)

model = Model()
agent = model.get_the_agent()

@app.route("/")
def index():
    """ This function renders Home page of the website
    """
    return render_template('index.html')


@app.route("/get", methods=["GET", "POST"])
def chat():
    """This function 
    """
    msg = request.form["msg"]
    input = msg
    default_prompt = read_prompt(file_path=prompt_file_path)
    default_prompt +=input
    print(input)
    result=agent.run(default_prompt)
    print(result)
    print("Response : ", result)
    return str(result)



if __name__ == '__main__':
    app.run(host="0.0.0.0", port= 8080, debug= True)
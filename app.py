import os
from os.path import join, dirname
from dotenv import load_dotenv

from flask import Flask, render_template, request, jsonify
import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

MONGODB_URI = os.environ.get("MONGODB_URI")
DB_NAME = os.environ.get("DB_NAME")

client = MongoClient(MONGODB_URI)
db = client[DB_NAME]

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/info', methods = ['GET'])
def tes_get():
    title_receive = request.args.get('title_give')
    print(title_receive)
    return jsonify({'result' : 'success', 'msg': 'GET Success!'})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)

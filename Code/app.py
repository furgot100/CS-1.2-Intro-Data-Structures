from flask import Flask, render_template, request, redirect, url_for
from sample import sentences
from analyzer import histogram_dict
from pymongo import MongoClient
import os

host = os.environ.get('MONGODB_URI', 'mongodb://localhost:27017/tweet-generator')
client = MongoClient(host=f'{host}?retryWrites=false')
db = client.get_default_database()
favorite = db.favorite


app = Flask(__name__)

@app.route('/')
def index():
    """Return Homepage"""
    text = 'texts/metamorphosis.txt'
    histogram = histogram_dict(text)
    sentence = sentences(histogram, 15)
    return render_template('index.html', tweet=sentence) 

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=os.environ.get('PORT', 5000))
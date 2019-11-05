from flask import Flask, render_template, request, redirect, url_for
from Code.sample import sentences
from Code.analyzer import histogram_dict

app = Flask(__name__)

@app.route('/')
def index():
    """Return Homepage"""
    text = 'Code/texts/metamorphosis.txt'
    histogram = histogram_dict(text)
    sentence = sentences(histogram, 15)
    return render_template('home.html', tweet=sentence) 


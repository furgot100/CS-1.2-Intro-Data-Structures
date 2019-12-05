from flask import Flask, render_template, request, redirect, url_for
from dictogram import read_file
from markov_chain import create_sentence, path


app = Flask(__name__)

@app.route('/')
def index():
    text = 'texts/metamorphosis.txt'
    words = read_file(text)
    sentence = create_sentence(path(words, 15))
    return render_template('home.html', tweet=sentence)


if __name__ == '__main__':
    app.run()

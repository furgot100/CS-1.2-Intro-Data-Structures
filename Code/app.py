from flask import Flask, render_template, request, redirect, url_for
from dictogram import read_file
from markov_chain import Markov


app = Flask(__name__)

@app.route('/')
def index():
    text = 'texts/1984.txt'
    markov = Markov(read_file(text), 20)
    sentence = markov.main()
    return render_template('home.html', tweet=sentence)


if __name__ == '__main__':
    app.run()

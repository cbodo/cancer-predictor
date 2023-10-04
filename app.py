from flask import Flask
from flask import render_template
from predictor import textboxes

app = Flask(__name__, template_folder='template')

@app.route('/')
def index():
    for textbox in textboxes:
        textbox.value = 0
    return render_template('index.html', textboxes=textboxes)
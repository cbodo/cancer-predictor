from flask import Flask
from flask import render_template
from textbox import TextBox

app = Flask(__name__, template_folder='template')

textboxes = [
    TextBox('radius_mean', 0, True),                # radius_mean
    TextBox('texture_mean', 0, True),               # texture_mean
    TextBox('perimeter_mean', 0, True),             # perimeter_mean 
    TextBox('area_mean', 0, True),                  # area_mean 
    TextBox('smoothness_mean', 0, True),            # smoothness_mean 
    TextBox('compactness_mean', 0, True),           # compactness_mean 
    TextBox('concavity_mean', 0, True),             # concavity_mean 
    TextBox('concave points_mean', 0, True),        # concave points_mean 
    TextBox('symmetry_mean', 0, True),              # symmetry_mean 
    TextBox('fractal_dimension_mean', 0, True)      # fractal_dimension_mean
]

@app.route('/')
def index():
    for textbox in textboxes:
        textbox.value = 0
    return render_template('index.html', textboxes=textboxes)

@app.route("/background/")
def background():
    return render_template('background.html')

@app.route("/about/")
def about():
    return render_template('about.html')
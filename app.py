from flask import Flask
from flask import render_template
from textbox import TextBox
from predictor import accuracy_score, generate_attribute_value, log_model, mse, scores_mean

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
    return render_template('background.html', accuracy_score=accuracy_score, mse=mse, scores_mean=scores_mean)

@app.route("/about/")
def about():
    return render_template('about.html')

@app.route("/random/")
def randomize():
    for textbox in textboxes:
        textbox.value = generate_attribute_value(textbox.name)
    return render_template('index.html', textboxes=textboxes)

@app.route("/predict/")
def predict():
    prediction = log_model.predict([[
        textboxes[0].value,
        textboxes[1].value,
        textboxes[2].value,
        textboxes[3].value,
        textboxes[4].value,
        textboxes[5].value,
        textboxes[6].value,
        textboxes[7].value,
        textboxes[8].value,
        textboxes[9].value,
        textboxes[0].value,
        textboxes[1].value,
        textboxes[2].value,
        textboxes[3].value,
        textboxes[4].value,
        textboxes[5].value,
        textboxes[6].value,
        textboxes[7].value,
        textboxes[8].value,
        textboxes[9].value,
        textboxes[0].value,
        textboxes[1].value,
        textboxes[2].value,
        textboxes[3].value,
        textboxes[4].value,
        textboxes[5].value,
        textboxes[6].value,
        textboxes[7].value,
        textboxes[8].value,
        textboxes[9].value
    ]])
    result = 'Benign' if prediction[0] == 0 else 'Malignant'
    return render_template('index.html', textboxes=textboxes, result=result)
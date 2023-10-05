from flask import Flask, render_template
import random
from textbox import TextBox
from predictor import accuracy_score, get_max, get_min, log_model, mse, scores_mean

app = Flask(__name__)

textboxes = [
    TextBox('radius_mean', 0, get_min('radius_mean'), get_max('radius_mean')),
    TextBox('texture_mean', 0, get_min('texture_mean'), get_max('texture_mean')),
    TextBox('perimeter_mean', 0, get_min('perimeter_mean'), get_max('perimeter_mean')), 
    TextBox('area_mean', 0, get_min('area_mean'), get_max('area_mean')), 
    TextBox('smoothness_mean', 0, get_min('smoothness_mean'), get_max('smoothness_mean')), 
    TextBox('compactness_mean', 0, get_min('compactness_mean'), get_max('compactness_mean')), 
    TextBox('concavity_mean', 0, get_min('concavity_mean'), get_max('concavity_mean')), 
    TextBox('concave points_mean', 0, get_min('concave points_mean'), get_max('concave points_mean')), 
    TextBox('symmetry_mean', 0, get_min('symmetry_mean'), get_max('symmetry_mean')), 
    TextBox('fractal_dimension_mean', 0, get_min('fractal_dimension_mean'), get_max('fractal_dimension_mean'))
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

@app.route("/contact/")
def contact():
    return render_template('contact.html')

@app.route("/random/")
def randomize():
    for textbox in textboxes:
        textbox.value = random.uniform(textbox.min, textbox.max)
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

if __name__ == '__main__':
    app.jinja_env.auto_reload = True
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(debug=True, host='127.0.0.1')
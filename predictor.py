import pandas as pd
import numpy as np
import random
from sklearn import linear_model, metrics, model_selection
from textbox import TextBox

COLUMN_NAMES = ['diagnosis', 'radius_mean', 'texture_mean', 'perimeter_mean', 'area_mean', 'smoothness_mean', 'compactness_mean', 'concavity_mean', 'concave points_mean', 'symmetry_mean', 'fractal_dimension_mean', 'radius_se', 'texture_se', 'perimeter_se', 'area_se', 'smoothness_se', 'compactness_se', 'concavity_se', 'concave points_se', 'symmetry_se', 'fractal_dimension_se', 'radius_worst', 'texture_worst', 'perimeter_worst', 'area_worst', 'smoothness_worst', 'compactness_worst', 'concavity_worst', 'concave points_worst', 'symmetry_worst', 'fractal_dimension_worst']

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


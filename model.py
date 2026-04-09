import numpy as np
from sklearn.linear_model import LinearRegression

hours = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)
scores = np.array([30, 40, 50, 65, 80])

model = LinearRegression()
model.fit(hours, scores)

def predict_score(study_hours):
    return int(model.predict([[study_hours]])[0])
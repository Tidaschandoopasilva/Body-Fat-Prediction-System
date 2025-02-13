from flask import Flask, request, render_template
import joblib
import numpy as np

model = joblib.load("bodyfat_model.pkl")

app = Flask(__name__)

def get_body_fat_category(body_fat):
    if body_fat < 6:
        return "Lean"
    elif 6 <= body_fat <= 24:
        return "Ideal"
    elif 25 <= body_fat <= 31:
        return "Average"
    else:
        return "Overfat"


@app.route('/')
def home():
    return render_template('index.html', age="", bmi="", prediction_text="", category_text="", error_text="")


@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Retrieve data from form
        age = request.form['age']
        bmi = request.form['bmi']

        if not age or not bmi:
            raise ValueError("Both fields are required.")

        age = float(age)
        bmi = float(bmi)

        # Prediction
        input_data = np.array([[age, bmi]])
        prediction = model.predict(input_data)[0]

        # Validate prediction range
        if prediction < 0 or prediction > 80:
            raise ValueError("Incorrect data. Please check your inputs.")

        # Get the body fat category
        category = get_body_fat_category(prediction)

        return render_template(
            'index.html',
            age=age,
            bmi=bmi,
            prediction_text=f"Predicted Body Fat Percentage: {prediction:.2f}",
            category_text=f"Category: {category}",
            error_text=""
        )
    except Exception as e:
        return render_template(
            'index.html',
            age=request.form['age'],
            bmi=request.form['bmi'],
            prediction_text="",
            category_text="",
            error_text=f"Error: {str(e)}"
        )


if __name__ == '__main__':
    app.run(debug=True)

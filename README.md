Body Fat Percentage Predictor
A Flask-based web application that predicts body fat percentage using Age and BMI. The app features a modern user interface, trained model deployment, and interactive functionality to categorize body fat into health ranges.

Features
Input & Prediction

Input Age and BMI to predict Body Fat Percentage.
Displays the predicted value along with a categorization: Lean, Ideal, Average, or Overfat.
Modern UI

Stylish interface with text boxes, buttons, and clean error messages.
Data retention when submitting predictions.
Error Handling

Ensures Body Fat Percentage stays within a valid range (0–80).
Displays error messages for invalid inputs.
Clear Option

A "Clear" button to reset input fields.
Health Categories
The predicted body fat percentage is categorized as follows:

Lean: 0–10%
Ideal: 10–20%
Average: 20–30%
Overfat: >30%
Technology Stack
Backend: Python, Flask
Frontend: HTML, CSS, Bootstrap for a modern and responsive UI
Machine Learning: Trained linear regression model (Scikit-learn)
Prerequisites
Python 3.10 or later
Required Python libraries:
bash
Copy
Edit
pip install flask scikit-learn pandas
Setup Instructions
Clone the repository:

bash
Copy
Edit
git clone https://github.com/your-repo/body-fat-predictor.git
cd body-fat-predictor
Place the trained model file (body_fat_model.pkl) in the root directory.

Run the Flask app:

bash
Copy
Edit
python app.py
Open your web browser and navigate to:

cpp
Copy
Edit
http://127.0.0.1:5000/
How to Use
Input Data

Enter Age and BMI values into the text boxes.
Predict

Click the Predict button to get the Body Fat Percentage and its category.
Clear

Click the Clear button to reset the input fields.
Error Messages

Enter valid numbers for Age and BMI to avoid errors.
Example Screenshot
(Include a screenshot of the application here)

Model Information
The linear regression model was trained using a dataset containing Age, BMI, and Body Fat Percentage.
Performance metrics of the trained model:

R² Score: X.XX
Root Mean Squared Error (RMSE): X.XX
Contributing
Contributions are welcome! Feel free to open issues or submit pull requests.

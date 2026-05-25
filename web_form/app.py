from flask import Flask, render_template, request
import csv

app = Flask(__name__)

# 1. Route to display the HTML form when someone visits the main page
@app.route('/')
def home():
    return render_template('form.html')

# 2. Route to handle the data when the user clicks "Submit"
@app.route('/submit', methods=['POST'])
def submit_data():
    # Grab the information typed into the HTML input fields
    name = request.form.get('user_name')
    @app.route('/submit', methods=['POST'])
def submit_data():
    name = request.form.get('user_name')
    phone = request.form.get('user_phone')
    
    # ADD THIS LINE TO SEE IT IN RENDER LOGS:
    print(f"NEW SUBMISSION -> Name: {name}, Phone: {phone}")
    
    with open('submissions.csv', mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([name, phone])
        
    return "<h1>Thank you! Your information has been saved successfully.</h1>"
    phone = request.form.get('user_phone')
    
    # Save the data into a local text file structured as a CSV spreadsheet
    with open('submissions.csv', mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([name, phone])
        
    return "<h1>Thank you! Your information has been saved successfully.</h1>"

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
    phone = request.form.get('user_phone')
    
    # 🌟 THIS IS THE NEW LINE YOU ARE ADDING:
    print(f"NEW SUBMISSION -> Name: {name}, Phone: {phone}", flush=True)
    
    # Save the data into a local text file structured as a CSV spreadsheet
    with open('submissions.csv', mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([name, phone])
        
    return "<h1>Thank you! Your information has been saved successfully.</h1>"

# 3. Force Render to use the correct port
if __name__ == '__main__':
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

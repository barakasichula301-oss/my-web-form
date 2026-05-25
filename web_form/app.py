from flask import Flask, render_template, request
import csv
import smtplib
from email.mime.text import MIMEText

app = Flask(__name__)

# 🔑 CONFIGURATION (Put your real info inside the quotes)
SENDER_EMAIL = "your-barakasichula301@gmail.com"      # The Gmail account sending the message
RECEIVER_EMAIL = "your-barakasichula301@gmail.com"    # Where you want to receive the alerts
APP_PASSWORD = "yhae nyol vplb ncjl"     # The App Password you just copied

# 1. Route to display the HTML form
@app.route('/')
def home():
    return render_template('form.html')

# 2. Route to handle data and send email
@app.route('/submit', methods=['POST'])
def submit_data():
    name = request.form.get('user_name')
    phone = request.form.get('user_phone')
    
    # --- EMAIL SENDING LOGIC ---
    subject = "New Form Submission! 🎉"
    body = f"You have a new submission:\n\nName: {name}\nPhone: {phone}"
    
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = SENDER_EMAIL
    msg['To'] = RECEIVER_EMAIL
    
    try:
        # Connect to Gmail's secure server
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(SENDER_EMAIL, APP_PASSWORD)
            server.sendmail(SENDER_EMAIL, RECEIVER_EMAIL, msg.as_string())
    except Exception as e:
        # If the email fails, it prints to logs so your app doesn't crash
        print(f"Email error: {e}")
    # ---------------------------

    # Keep this so it still writes to CSV locally just in case
    with open('submissions.csv', mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([name, phone])
        
    return "<h1>Thank you! Your information has been saved successfully.</h1>"

if __name__ == '__main__':
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

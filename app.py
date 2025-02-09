from flask import Flask, request, jsonify
from flask_cors import CORS
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = Flask(__name__)
CORS(app)  # Allows requests from React/Postman

@app.route('/', methods=['GET'])
def home():
    return jsonify({"message": "Flask server is running!"}), 200

@app.route('/send-email', methods=['POST'])
def send_email():
    try:
        data = request.get_json()  # Get JSON data from request

        name = data.get('name')
        email = data.get('email')
        date = data.get('date')
        time = data.get('time')

        # Email credentials (use environment variables in production)
        EMAIL_ADDRESS = "mbrkaushik@gmail.com"
        EMAIL_PASSWORD = "xenk izbp cimk xdgj"  # Use App Password, not your real password

        subject = "New Meeting Request"
        body = f"Name: {name}\nEmail: {email}\nPreferred Date: {date}\nPreferred Time: {time}"

        msg = MIMEMultipart()
        msg["From"] = EMAIL_ADDRESS
        msg["To"] = EMAIL_ADDRESS  # Sending email to yourself
        msg["Subject"] = subject
        msg.attach(MIMEText(body, "plain"))

        # SMTP setup for Gmail
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.sendmail(EMAIL_ADDRESS, EMAIL_ADDRESS, msg.as_string())

        return jsonify({"message": "Email sent successfully!"}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)

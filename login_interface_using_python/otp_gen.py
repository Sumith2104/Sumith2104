import smtplib
import random

def generate_otp():
    return str(random.randint(100000, 999999))

def send_otp_via_email(email, one_time_passcode, user_name, password, log_id):
    sender_email = ""        #<------- your email (sender email with 2 step auth)
    sender_password = ""     #<------- your gmail app password
    subject = "Your OTP Code"
    body = f"Hi {user_name},\n\nYour OTP is: {one_time_passcode}\nIt will despawn in a few minutes."
    message = f"Subject: {subject}\n\n{body}"

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, email, message)
        print(f"OTP sent successfully to {user_name}!")
    except Exception as e:
        print(f"Error sending OTP: {e}")
        exit("Try again!")

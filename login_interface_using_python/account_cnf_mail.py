import smtplib

def send_confirmation_email(user_info):
    if not user_info:
        print("Error: No user information provided!")
        return

    sender_email = ""         #<------- your email (sender email with 2 step auth)
    sender_password = ""      #<------- your gmail app password

    subject = "Account Successfully Created"
    body = f"""Hi {user_info['name']},

Your account has been successfully created!

You can log in with the following credentials:

 LOGIN ID: {user_info['log_id']}  
 PASSWORD: {user_info['password']}

Thank you for registering!
"""
    message = f"Subject: {subject}\n\n{body}"

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, user_info["email"], message)
        print("Please check your Gmail inbox for the confirmation email!")
    except Exception as e:
        print(f"Error sending confirmation email: {e}")
        exit("Try again!")

if __name__ == "__main__":
    import main
    acc_status = main.reg_c()

    if acc_status and "user" in acc_status:
        send_confirmation_email(acc_status["user"])
    else:
        print("Registration failed. No confirmation email sent.")

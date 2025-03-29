from datetime import datetime
import random
import smtplib
import time

account_creation = False

def loading_animation():
    print(f"Please wait", end = "")
    time.sleep(1)
    print(".", end = "")
    time.sleep(1.4)
    print(".", end = "")
    time.sleep(1)
    print(".", end = "")
    time.sleep(1.5)

def generate_otp():
    return str(random.randint(100000, 999999))

def send_otp_via_email(email, one_time_passcode):
    sender_email = "Your Email"                         #<------ sender email
    sender_password = "Email app password"              #<------ app password
    subject = "Your OTP Code"
    body = f"Your OTP is: {one_time_passcode}"
    message = f"Subject: {subject}\n\n{body}"

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, email, message)
        print("OTP sent successfully!")
    except Exception as e:
        print(f"Error sending OTP: {e}")
        exit("Try again!!")

def get_current_time():
    return datetime.now().strftime("%H:%M:%S")

def get_current_date():
    return datetime.now().strftime("%Y-%m-%d")

def password_generator():
    strings = "abcdefghijklmnopqrstuvwxyz"
    numbers = "1234567890"
    special_char = "!@#$%^&*()"

    num_for_char_count = 5

    for_char = random.sample(strings,num_for_char_count)
    for_num = random.sample(numbers,num_for_char_count)
    for_special = random.sample(special_char,num_for_char_count)

    combined = for_char + for_num + for_special
    random.shuffle(combined)
    mylist = ''.join(combined)

    return mylist

def log_data_db():
    user_name = input("Enter your name: ")
    phone = input("Enter your phone number: ")
    log_id = f"{user_name[:4]}{phone[5:]}"
    dob = input("Date of birth: ")
    email = input("Enter your email: ")

    curr_time = get_current_time()
    curr_date = get_current_date()

    password_choice = input("We can generate a password for you. Can we? (Y/N): ").upper()

    if password_choice == "Y":
        password = password_generator()
    else:
        password = input("Enter password: ")
        cnf_pass = input("Confirm password: ")
        if password == cnf_pass:
            send_otp_via_email(email, generate_otp())
        else:
            print("Passwords do not match. Try again.")
            return None

    send_otp_via_email(email, generate_otp())

    return {
        "log_id" : log_id,
        "name": user_name,
        "phone": phone,
        "dob": dob,
        "email": email,
        "password": password,
        "log_time" : curr_time,
        "log_date" : curr_date
    }

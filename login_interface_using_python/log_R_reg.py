import getpass

def get_current_time():
    from datetime import datetime
    return datetime.now().strftime("%H:%M:%S")

def get_current_date():
    from datetime import datetime
    return datetime.now().strftime("%Y-%m-%d")

def password_generator():
    import random
    import string
    return ''.join(random.choices(string.ascii_letters + string.digits, k=8))

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
        password = getpass.getpass("Enter password: ")
        cnf_pass = getpass.getpass("Confirm password: ")
        if password != cnf_pass:
            print("Passwords do not match. Try again.")
            return None

    return {
        "log_id": log_id,
        "name": user_name,
        "phone": phone,
        "dob": dob,
        "email": email,
        "password": password,
        "log_time": curr_time,
        "log_date": curr_date
    }

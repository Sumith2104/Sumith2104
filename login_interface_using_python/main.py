import log_R_reg
import otp_gen
import pandas as pds
import gc
import account_cnf_mail
import os
import random

def reg_c():
    final_data_set = []
    user_info = log_R_reg.log_data_db()

    if not user_info:
        print("User registration failed.")
        return

    final_data_set.append(user_info)

    otp = otp_gen.generate_otp()
    otp_gen.send_otp_via_email(user_info["email"], otp, user_info["name"], user_info["password"], user_info["log_id"])

    user_input = input("\nEnter the OTP received: ")

    if user_input == otp:
        print("OTP Verified Successfully!")
        log_R_reg.account_creation = True
        account_cnf_mail.send_confirmation_email(user_info)

    else:
        print("Invalid OTP. Please try again.")
        log_R_reg.account_creation = False

    if log_R_reg.account_creation:
        file_path = r""         #<---------- actual file full path for csv append

        try:
            df = pds.DataFrame(final_data_set)
            df.to_csv(file_path, mode='a', index=False, header=not os.path.exists(file_path))
            print("Account data saved successfully!")
        except Exception as e:
            print(f"Error saving account data: {e}")

        gc.collect()
    else:
        exit("Account creation failed!")

    return {"user": user_info}

def log_or_reg():
    choice = input("Do you want to \n(1) Register \n(2) Login? ")

    if choice == "1":
        reg_c()
    elif choice == "2":
        print("Login functionality is not yet implemented.")
    else:
        print("Invalid choice. Try again.")

# Run the program
log_or_reg()

if __name__ == '__main__':
    log_or_reg()

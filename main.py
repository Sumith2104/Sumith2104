from data_science.Log_DB import log_R_reg
from pandas import pandas as pds
import gc as cache_collector

def reg_c():
    final_data_set = []

    user_info = log_R_reg.log_data_db()
    final_data_set.append(user_info)

    if user_info:
        otp = log_R_reg.generate_otp()
        log_R_reg.send_otp_via_email(user_info["email"], otp)

        user_input = input("\nEnter the OTP received: ")
        if user_input == otp:
            print("OTP Verified Successfully!")
            log_R_reg.account_creation = True
        else:
            print("Invalid OTP. Please try again.")
            log_R_reg.account_creation = False

    if log_R_reg.account_creation:
        df = pds.DataFrame(final_data_set)
        df.to_csv(fr"C:\Users\sumit\PycharmProjects\PythonProject\data_science\login_db.csv", mode='a', index=False,
                  header=False, chunksize=500)
        cache_collector.collect()
    else:
        exit("Account creation failed!!!")

def log_or_reg():
    us_inp = int(input("Welcome\n1.Log_in\n2.Register\nEnter your selection: "))
    if us_inp == 1:
        print()
    elif us_inp == 2:
        reg_c()
    else:
        return
if __name__ == '__main__':
    log_or_reg()
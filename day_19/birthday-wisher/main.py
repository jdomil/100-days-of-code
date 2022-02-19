import pandas as pd
from datetime import datetime
import random
import smtplib

MY_EMAIL = "smtp.python.100@gmail.com"
MY_PASSWORD = "AbCd_1234"


def trigger_email(email_data):
    """Sends email with the information for the corresponding birthday person"""
    letter_choice = random.randint(1, 3)
    file_path = f"letter_templates/letter_{letter_choice}.txt"

    with open(file_path) as letter_file:
        letter_content = letter_file.read()
        custom_letter = letter_content.replace("[NAME]", email_data["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=email_data["email"],
            msg=f"Subject:Happy Birthday!\n\n{custom_letter}"
        )


# Read birthdays file and identify if it's someone's birthday
today = datetime.now()
today_tuple = (today.month, today.day)

birthdays_file = pd.read_csv("birthdays.csv")
birthdays_dict = {(birthday["month"], birthday["day"]): birthday for (index, birthday) in birthdays_file.iterrows()}

if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    trigger_email(birthday_person)


# 1. Update the birthdays.csv
# 2. Check if today matches a birthday in the birthdays.csv
# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
# 4. Send the letter generated in step 3 to that person's email address.





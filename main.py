
from datetime import datetime
import pandas
import random
import smtplib

print('HELLO :)')
MY_EMAIL = "roudasaffuri@gmail.com"
MY_PASSWORD = "**** **** **** ****"

today = datetime.now()
today_tuple = (today.month, today.day)

data = pandas.read_csv("birthdays.csv")

birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}
#birthdays_dict = {(data_row.month, data_row.day): data_row["name"] for (index, data_row) in data.iterrows()}
#print(birthdays_dict)

if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        # replace() method:
        # txt = 'I like bananas'
        # txt = txt.replace('bananas','apples')
        # you have to save it to a new variable in order to see the replaced
        contents = contents.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=birthday_person["email"],
            msg=f"Subject:Happy Birthday!\n\n{contents}"
        )

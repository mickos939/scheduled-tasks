# 1. Change MY_EMAIL/MY_PASSWORD to your own details.
# 2. Go to your email provider and make it allow less secure apps.
# 3. Update the SMTP ADDRESS to match your email provider.


import os
import smtplib
import datetime as dt
import random

# import os and use it to get the Github repository secrets
MY_EMAIL = os.environ.get("MY_EMAIL")
MY_PASSWORD = os.environ.get("MY_PASSWORD")

now = dt.datetime.now()
weekday = now.weekday()
#if weekday == 1:
with open("quotes.txt") as quote_file:
    all_quotes = quote_file.readlines()
    quote = random.choice(all_quotes)
print(quote)

connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user=MY_EMAIL, password=MY_PASSWORD)
connection.sendmail(
    from_addr=MY_EMAIL,
    to_addrs="michael.bergman@katrineholm.se",
    msg=f"Subject:Dagens citat\n\nHej! Här är ett tänkvärt citat:\n\n{quote}".encode("utf-8")
)
connection.close()

import smtplib
import datetime as dt
import random

my_email = "amitgupta16042002@gmail.com"
password = "kuunsueagzkzgjyg"

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 1:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="sonaliagrwal31011997@gmail.com",
            msg=f"Subject:Tuesday Motivation\n\n{quote}"
        )







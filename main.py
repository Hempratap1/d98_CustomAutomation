import csv
import os
import random
import datetime as dt
import smtplib

# Creating a list to store authors and quotes
authors = []
quotes = []


# Function to send emails
def email(quote):
    my_email = os.getenv("email")
    password = os.getenv("password")

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=my_email,
            msg=f"Subject:MOTIVATION \n\n{quote}"
        )


# Opening the csv and read the data
with open("quotes.csv", mode='r', newline='') as file:
    reader = csv.DictReader(file)
    for row in reader:
        authors.append(row['Author'])
        quotes.append(row['Quote'])

# Generating a random quote within the quotes
n = random.randint(1, len(authors))
quote_of_the_day = f"{quotes[n]}\n-{authors[n]}".title()
print(quote_of_the_day)


# Get the current time
current_time = dt.datetime.now()

# Check if the current time is 6:00 AM
if current_time.hour == 6 and current_time.minute == 0:
    # Put your code here that you want to run at 6:00 AM
    email(quote=quote_of_the_day)


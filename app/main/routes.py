from flask import render_template
from . import main
import smtplib


@main.route("/", methods= ["GET", "POST"])
def home():
    # """Sending the articles via email"""
    # my_email = "sayomilembo@gmail.com"
    # my_password = "your_password"
    # message_body = "email message"
    #
    # with smtplib.SMTP("smtp.gmail.com", 587) as connection:
    #     connection.starttls()
    #     connection.login(user=my_email,
    #                      password=my_password)
    #     connection.sendmail(
    #         from_addr=my_email,
    #         to_addrs="rzedits@yahoo.com",
    #         msg=f"Subject: Here are top news from Unherd \n\n {
    #         message_body}"
    #     )
    return render_template("index.html")

@main.route("/bulls")
def bulls():
    return render_template("bulls.html")

@main.route("/podcasts")
def podcasts():
    return render_template("podcast.html")



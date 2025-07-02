from flask import render_template, abort
from . import main
import smtplib
import requests


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

@main.route("/articles/<int:post_id>")
def articles(post_id):
    new_id = post_id - 1
    posts = requests.get("https://api.npoint.io/2e85288c3d7b98781faa").json()
    articles = posts["articles"]
    for post in articles:
        if post.get("post_id") ==  str(post_id):
            selected_post = articles[new_id]
            print(selected_post)

        if not selected_post:
          abort(404)  # Return 404 page if not found

    return render_template("articles.html", post=selected_post)

@main.route("/podcasts")
def podcasts():
    return render_template("podcast.html")

"""Routes for the diffrent categories of videos"""
@main.route("/kingdom_videos")
def kingdom_videos():
    return render_template("kingdom_videos.html")

""" Healing streams route"""
@main.route("/anointing_streams")
def anointing_streams():
    return render_template("anointing_streams.html")

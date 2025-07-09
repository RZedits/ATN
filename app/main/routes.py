from flask import render_template, abort
from . import main
from app.models import Articles
from app import db
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField,DateField, SubmitField
from wtforms.validators import DataRequired
from flask_ckeditor import CKEditorField

# WTForm for new article
class Article(FlaskForm):
    author = StringField("Author's name", validators=[DataRequired()])
    title = StringField("Post title", validators=[DataRequired()])
    post_photo = StringField("Photo url", validators=[DataRequired()])
    author_url = StringField("Author url", validators=[DataRequired()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    day = DateField("Date", validators=[DataRequired()])
    submit = SubmitField("Submit")


@main.route("/", methods= ["GET", "POST"])
def home():
    return render_template("index.html")

@main.route("/bulls")
def bulls():
    return render_template("bulls.html")

@main.route("/create_article", methods = ["GET", "POST"])
def create_article():
    form = Article()
    if form.validate_on_submit():
        new_article = Articles(
            author=form.author.data,
            title = form.title.data,
            post_photo= form.post_photo.data,
            author_url = form.author_url.data,
            day= form.day.data,
            body = form.body.data
        )
        db.session.add(new_article)
        db.session.commit()
        return "sucess"
    return render_template("create_article.html", form= form)

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

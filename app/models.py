from . import db
from sqlalchemy import Integer, String, Date, Text, Float
from sqlalchemy.orm import relationship, Mapped, mapped_column
from datetime import date

class Articles(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    title: Mapped[str] = mapped_column(String(250), nullable=False)
    post_photo: Mapped[str] = mapped_column(String(250), nullable=True)
    author_url: Mapped[str] = mapped_column(String(250), nullable=True)
    day: Mapped[date] = mapped_column(Date, nullable=False)
    body: Mapped[str] = mapped_column(String(2500), nullable=False)

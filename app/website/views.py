from . import website
from flask import render_template


@website.route("/")
def home():
    return render_template("website/home.html")

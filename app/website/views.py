from . import website
from flask import render_template
from flask_login import login_required

@login_required
@website.route("/painel")
def dashboard():
    return render_template("website/dashboard.html")
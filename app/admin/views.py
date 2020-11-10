from . import admin
from flask import render_template
from flask_login import login_required
from .utils import admin_required


@admin.route("/")
@login_required
@admin_required
def home():
    return render_template("admin/dashboard.html")
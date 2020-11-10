from flask import flash, redirect, url_for
from functools import wraps
from flask_login import current_user


def admin_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        admin = current_user.is_admin
        if not admin:
            flash("Você precisa ser admin para acessar este recurso")
            return redirect(url_for('website.dashboard'))
        return f(*args, **kwargs)
    return decorated

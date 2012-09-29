from functools import wraps
from flask import g, request, abort, redirect, url_for, flash

def ajax_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):

        if not request.is_xhr:
            return abort(400)
        return f(*args, **kwargs)

    return decorated

def requires_login(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if g.user is None:
            flash(u'Necesitas estar logueado para acceder esta pagina')
            return redirect(url_for('login', next=request.path))
        return f(*args, **kwargs)

    return decorated

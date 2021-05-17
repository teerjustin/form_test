from flask import render_template, redirect, request, session, flash

from flask_app import app
from ..models.dojo import Dojo

@app.route('/')
def index():
    return render_template("index.html")

# @app.route('/result')
# def result():
#     print('THIS IS DOJO ID **************************************', dojo_id)
#     return render_template("show.html")


@app.route('/create', methods = ["POST"])
def create_user():
    if not Dojo.validate_dojo(request.form):
        # redirect to the route where the burger form is rendered.
        return redirect('/')
    # else no errors:
    dojo = Dojo.create(request.form)
    return render_template("show.html", dojo = dojo)



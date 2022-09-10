from flask_app import app
from flask_app.models import ninja_model
from flask import redirect, render_template, request




@app.route('/ninja/create', methods = ['POST'])
def create_ninja():
    data = {
        **request.form
    }
    ninja_model.Ninja.create(data)
    return redirect('/')


@app.route('/show_ninja')
def show_ninjas():
    all_ninjas = ninja_model.Ninja.get_all()
    return render_template('show_ninja.html', all_ninjas=all_ninjas)


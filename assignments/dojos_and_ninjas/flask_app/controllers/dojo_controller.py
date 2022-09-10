from flask_app import app
from flask import render_template, request,redirect
from flask_app.models.dojo_model import Dojo
from flask_app.models.ninja_model import Ninja

@app.route('/')
def index():
    all_dojos = Dojo.get_all()
    return render_template('dojos.html',all_dojos=all_dojos)

@app.route('/ninjas/new')
def new_ninja_form():
    all_dojos = Dojo.get_all()
    return render_template('new_ninja.html', all_dojos=all_dojos)


@app.route('/dojo/create', methods=['post'])
def create_dojo():
    Dojo.create({'name': request.form['name']})
    return redirect('/') 


@app.route('/dojo/show/<int:dojo_id>')
def show_ninja(dojo_id):
    dojo = Dojo.get_dojo_and_ninjas({'id':dojo_id})
    print('========================')
    print(dojo)
    return render_template('show_ninja.html', dojo=dojo)




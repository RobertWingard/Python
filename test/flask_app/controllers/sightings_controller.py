from flask_app import app
from flask import render_template,redirect,request,flash,session
from flask_app.models.user_model import User
from flask_app.models.sighting_model import Sighting


@app.route('/sightings/new')
def new_sighting_form():
    if 'user_id' not in session:
        return redirect('/')
    # logged_user = User.get_by_id({'id':session[user_id']})
    return render_template('sightings_new.html')


@app.route('/sightings/create', methods=['POST'])
def process_sighting():
    if 'user_id' not in session:
        return redirect('/')
        
    if not Sighting.validator(request.form):
        
        return redirect('/sightings/new')
    data = {
        **request.form,
        'user_id': session['user_id']
        
    }
    
    id = Sighting.create(data)
    
    return redirect('/dashboard')



@app.route('/sightings/<int:id>/edit')
def edit_sighting_form(id):
    if 'user_id' not in session:
        return redirect('/')
    this_sighting = Sighting.get_by_id({'id': id})
    if not int(session['user_id']) == this_sighting.user_id:
        flash('whoa there')
        return redirect('/dashboard')
    sighting = Sighting.get_by_id({'id':id})
    return render_template('sightings_edit.html', sighting=sighting)


@app.route('/sightings/<int:id>/update', methods=['POST'])
def update_sighting(id):
    if 'user_id' not in session:
        return redirect('/')
    this_party = Sighting.get_by_id({'id': id})
    if not int(session['user_id']) == this_party.user_id:
        flash('watch out')
        return redirect('/dashboard')
    if not Sighting.validator(request.form):
        return redirect(f'/sightings/{id}/edit')
    data = {
        **request.form,
        'id': id
    }
    Sighting.update(data)
    return redirect('/dashboard')



@app.route('/sightings/<int:id>')
def show_sighting(id):
    sighting = Sighting.get_by_id({'id' : id})
    user_data = {
        'id': session['user_id']
    }
    logged_user = User.get_by_id(user_data)
    return render_template('sightings_one.html', sighting=sighting, logged_user=logged_user)



@app.route('/sightings/<int:id>/delete')
def del_sighting(id):
    if 'user_id' not in session:
        return redirect('/')
    this_party = Sighting.get_by_id({'id': id})
    if not int(session['user_id']) == this_party.user_id:
        flash('whoa there, thats not yours')
        return redirect('/welcome')
    Sighting.delete({'id':id})
    return redirect('/dashboard')


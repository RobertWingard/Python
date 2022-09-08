from flask import Flask, render_template, request, redirect, session
from dog_model import Dog

app = Flask(__name__)
app.secret_key = ''



@app.route('/')
def index():
    all_dogs = Dog.get_all()
    return render_template('index.html',all_dogs=all_dogs)


@app.route('/dogs/<int:id>')
def one_dog(id):
    one_dog = Dog.get_one({'id':id})
    return render_template('one_dog.html', one_dog=one_dog)

@app.route('/dogs/new')
def new_dog_form():
    return render_template('dogs_new.html')


@app.route('/dogs/create', methods=['POST'])
def create_dog():
    Dog.create(request.form)
    return redirect('/')


@app.route('/dogs/<int:id>/edit')
def edit_dog_form(id):
    data = {
        'id':id
    }
    this_dog = Dog.get_one(data)
    return render_template('dogs_edit.html', this_dog=this_dog)


@app.route('/dogs/<int:id>/update', methods=['POST'])
def update_dog(id):
    data = {
        **request.form, # quick way to copy the contests of request.form into this dictionary
        'id':id 
    }
    Dog.update(data)
    return redirect('/')


@app.route('/dogs/<int:id>/delete')
def delete_dog(id):
    data = {
        'id':id
    }
    Dog.delete(data)
    return redirect('/')








if __name__=='__main__':
    app.run(debug=True)

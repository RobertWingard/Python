from flask import Flask, render_template, request, redirect, session
from users import User


app = Flask(__name__)
app.secret_key = ''

@app.route('/')
def index():
    all_users = User.get_all()            #this one is from template
    print(all_users)
    return render_template('read.html', t=all_users)


@app.route('/show_one/<int:id>') #this will be the routes path that needs to be taken to get back here.
def one_user(id):
    data = {
        'id': id
    }
    one_user = User.show_one(data)
    return render_template('one_user.html', one_user=one_user) #suply the name of the templates from the folder
                                            #this ^ is the data I want to process in there.
@app.route('/create',methods=['POST'])
def create_user():
    print(request.form)
    User.create(request.form)
    return redirect('/')

@app.route('/createNew')
def createNew():
    return render_template("create.html")

@app.route('/delete/<int:id>')
def delete(id):
    data = {
        'id': id
    }
    User.delete(data)
    return redirect('/')


@app.route('/user/<int:id>/edit')
def edit_user_form(id):
    data = {
        'id':id
    }
    this_user = User.show_one(data)
    return render_template('edit.html', this_user=this_user)

@app.route('/user/<int:id>/update', methods=['POST'])
def update_user(id):
    data = {
        **request.form, # quick way to copy the contests of request.form into this dictionary
        'id':id 
    }
    User.update(data)
    return redirect('/')








if __name__=="__main__":
    app.run(debug=True)

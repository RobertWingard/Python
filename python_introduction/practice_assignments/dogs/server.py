from flask_app import app
from flask_app.controllers import dogs_controller, awards_controll


if __name__=='__main__':
    app.run(debug=True)

from flask import Flask  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"

@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return 'first page!'  # Return the string 'Hello World!' as a response

@app.route('/dojo')
def dojo():
    return 'Dojo'

@app.route('/say/<word>')
def show_word(word):
    return 'Hi ' + str(word)


@app.route('/repeat/<int:number>/<word>')
def multi(number, word):
    return int(number) * str(word)

@app.errorhandler(404)
def not_found(e):
    return 'Sorry! No response. Try again.'





if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.


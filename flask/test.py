from flask import Flask, render_template, request, redirect, session

app = Flask(name)
app.secret_key = ''

@app.route('/')
def index():
    return render_template('index.html')

if name=='main':
    app.run(debug=True)

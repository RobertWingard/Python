from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def index():
    return render_template("index.html", h=100, w=100, color='blue',)	# notice the 2 new named arguments!


@app.route('/play')
def play():
    return render_template('index.html', h=100, w=100, color='blue')

@app.route('/play/<int:number>')
@app.route('/play/<int:number>/<color>')
def multi(number, color='blue'):
    return render_template('index.html', color=color, number=number) 

















if __name__=="__main__":
    app.run(debug=True)


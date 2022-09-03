from flask import Flask, render_template,request,session,redirect

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")	# notice the 2 new named arguments!


@app.route('/result',methods=['POST'])
def results():
    session['name'] = request.form['name']
    print(session['name'])
    return redirect('results.html')

@app.route('/results')
def real_results():
    
    return render_template('results.html')














if __name__=="__main__":
    app.run(debug=True)
from flask import Flask, render_template,request,session,redirect
import random
app = Flask(__name__)
app.secret_key = 'keep safe'

@app.route('/')
def index():
    if 'gold' not in session:
        session['gold']= 0
    return render_template("index.html")

@app.route('/process_money', methods=['POST'])
def process():
    farm = random.randint(0,100)
    cave = random.randint(15,50)
    house = random.randint(20,30)
    casino = random.randint(-750,500)


    if 'activities' not in session:
        session['activities'] = [ ]

    if 'name' not in session:
        session['name'] = request.form['name']
        print(session['name'])
    else:
        session.pop('name')
        session['name'] = request.form['name']
        print(session['name'])
    if session['name'] == 'farm':
        session['gold'] += farm
        session['activities'].append(f'You have done some farming and collected {farm} gold')   
    elif session['name'] == 'cave':
        session['gold'] += cave
        session['activities'].append(f'You have done some mining and collected {cave} gold')
    elif session['name'] == 'house':
        session['gold'] += house
        session['activities'].append(f'You have cleaned house and collected {house} gold') 
    elif session['name'] == 'casino':
        session['gold'] += casino
        if casino < 0:
            session['activities'].append(f"<p id='red'> The casino takes {casino} gold </p>")
        else:
            session['activities'].append(f"The casino pays out {casino} gold")

        
            


    return redirect('/')

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')



if __name__=="__main__":
    app.run(debug=True)


















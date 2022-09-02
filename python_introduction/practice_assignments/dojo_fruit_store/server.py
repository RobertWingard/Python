from flask import Flask, render_template, request, redirect
app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    print(request.form)
    cust = request.form['first_name']
    last_name = request.form['last_name']
    apple = request.form['apple']
    strawberry = request.form['strawberry']
    raspberry = request.form['raspberry']
    count = int(apple)+int(strawberry)+int(raspberry)
    print(f'hello there {cust} you have purchased {count} fruits')
    return render_template("checkout.html", cust=cust, count=count, last_name=last_name, apple=apple,strawberry=strawberry,raspberry=raspberry)

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    
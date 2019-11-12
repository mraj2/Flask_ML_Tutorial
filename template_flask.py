'''
/template_flask.py
/templates
    /hello.html
'''
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("add_mul.html")

@app.route('/operation', methods = ['POST', 'GET'])
def operation():
    if request.method == 'POST':
        a = request.form['a']
        b = request.form['b']
       
        add_val = int(a) + int(b)
        print("addition: ", add_val)

        mul_val = int(a) * int(b)
        print("multiplication: ", mul_val)

        return render_template('result.html', add = add_val, mul = mul_val)

if __name__ == '__main__':
   app.run(debug = True)
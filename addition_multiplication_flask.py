#################### Notes ###############################
# Advance REST Client POST request check
# Chrome extention: add Advance REST Client extention in your browser
# Open Advance REST Client
# Select Request Method: POST
# Add Request URL: http://127.0.0.1:5001/operation
# Goto Body part 
# Select Content type: Form data
# and Add Form data parameters: a and b.
##########################################################

from flask import Flask, redirect, url_for, request

app = Flask(__name__)

@app.route('/operation', methods = ['POST', 'GET'])
def operation():
    if request.method == 'POST':
        a = request.form['a']
        b = request.form['b']
       
        add_val = int(a) + int(b)
        print("addition: ", add_val)

        mul_val = int(a) * int(b)
        print("multiplication: ", mul_val)

        return f"addition is: {add_val}   multiplication is :{mul_val}"
    

if __name__ == '__main__':
    app.run(host ="0.0.0.0", port = 5001 ,debug = True)
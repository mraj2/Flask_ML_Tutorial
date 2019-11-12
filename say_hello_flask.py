# Importing flask module in the project is mandatory. 
# An object of Flask class is our WSGI application.
from flask import Flask

# Flask constructor takes the name of current module (__name__) as argument.
app = Flask(__name__)

print(app, "app")

# The route() function of the Flask class is a decorator, 
# The route() decorator in Flask is used to bind URL to a function
# which tells the application which URL should call the associated function.
# 
#             app.route(rule, options)
#
# rule parameter: represents URL binding with the function.
# options: GET, POST methods to receive input objects and send output objects.

@app.route('/')
def welcome():
    return "Welcome to page"

################################# Notes ##################################

# Here, URL ‘/hello’ rule is bound to the hello_world() function. 
# As a result, if a user visits http://localhost:5000/hello URL, 
# the output of the hello_world() function will be rendered in the browser.

##########################################################################

@app.route('/hello')
def hello_world():
   return 'Hello World! I am Flask!'

# run() method of Flask class runs the application on the local development server.
#
#               app.run(host, port, debug, options)
# 
# All parameters are optional
# host   : Hostname to listen on. Defaults to 127.0.0.1 (localhost). Set to ‘0.0.0.0’ to have server available externally
# port   : Defaults to 5000
# debug  : Defaults to false. If set to true, provides a debug information
# options: To be forwarded to underlying Werkzeug server.


if __name__ == '__main__':
   app.run(debug = True)
   #app.run(host = '0.0.0.0', port = 5001, debug = False)

# variable part is marked as 
# 
#        <variable-name>
# 
# It is passed as a keyword argument to the function with which the rule is associated.
# 
# <int:Variable-name>, <float:Variable-name>

# @app.route('/hello/<name>')
# def hello_name(name):
#    return 'Hello %s!' % name


# if __name__ == '__main__':
#    app.run(debug = True)

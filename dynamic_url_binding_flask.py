################################# Notes ##################################
from flask import Flask, redirect, url_for

# url_for() function : very useful for dynamically building a URL for a specific function. 
#                      first argument : the name of a function
#                      and one or more keyword arguments: each corresponding to the variable part of URL.
#
# redirect() function: redirect current url to specific function url
##########################################################################
#from flask import Flask, redirect, url_for
app = Flask(__name__)

@app.route('/admin')
def hello_admin():
   return 'Hello Admin'

@app.route('/guest/<guest>')
def hello_guest(guest):
   return 'Hello %s as Guest' % guest

@app.route('/user/<name>')
def hello_user(name):
   if name =='admin':
      return redirect(url_for('hello_admin'))
   else:
      return redirect(url_for('hello_guest',guest = name))

if __name__ == '__main__':
   app.run(debug = True)
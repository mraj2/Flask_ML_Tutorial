# Different methods of data retrieval from specified URL 
# are defined in HTTP protocol.

################# Methods & Description ##############################################

# GET : Sends data in unencrypted form to the server. Most common method.
# HEAD: Same as GET, but without response body
# POST: Used to send HTML form data to server. Data received by POST method is not cached by server.
# PUT : Replaces all current representations of the target resource with the uploaded content.
# DELETE : Removes all current representations of the target resource given by a URL

################# attributes of request object ########################################

# Form − dictionary object containing key and value pairs of form parameters and their values.
# args − parsed contents of query string which is part of URL after question mark (?).
# Cookies − dictionary object holding Cookie names and values.
# files − data pertaining to uploaded file.
# method − current request method.

#######################################################################################

from flask import Flask, redirect, url_for, request
app = Flask(__name__)

@app.route('/success/<name>')
def success(name):
   return 'welcome %s' % name

@app.route('/login',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      user = request.form['nm']
      return redirect(url_for('success',name = user))
   else:
      user = request.args.get('nm')
      return redirect(url_for('success',name = user))

if __name__ == '__main__':
   app.run(host ="0.0.0.0", port = 5001 ,debug = True)

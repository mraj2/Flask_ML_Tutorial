# Flask_ML_Tutorial
GOAL :- Using Flask web application framework to serve as API request and deploy your application in production.

### Create Virtual Envrionment and Install Requirements

* virtualenv --python=python3.6 env

* source env/bin/activate

* pip install -r requirements.txt

* pip install flask

### step 0: Hello World 
* python3 say_hello_flask.py

### step 1: Dynamic url binding
* python3 dynamic_url_binding_flask.py

### step 2: HTTP methods
* python3 http_methods_flask.py

### step 3: HTTP methods example 
* python3 addition_multiplication_flask.py

### step 4: Using Advance REST Client to Test Webserver request and response

* Advance REST Client POST request check
* Chrome extention: add Advance REST Client extention in your browser
* Open Advance REST Client
* Select Request Method: POST
* Add Request URL: http://127.0.0.1:5001/operation
* Goto Body part 
* Select Content type: Form data
* and Add Form data parameters: a and b.

### step 5: Rendering Dynamic Webpages using Zinja-2 template
Format:
 * ---/template_flask.py 
 * ---/templates
 * -------/add_mul.html
Run 
* python3 template_flask.py

### step 6: Dog - Cat classifier
already done below steps 
* git clone https://github.com/ardamavi/Dog-Cat-Classifier.git
* cd Dog-Cat-Classifier/
* pip install -r requirements.txt
* cd ../Dog-Cat-Classifier

Run WebServer for Dog-Cat Classifier

* python3 Dog-Cat-Classifier_server.py 

### step 7: preview for before hosting web application in global domain, to check all functionalities in web application and web server.   

download ngrok
* https://ngrok.com/download

give which port you assign in your web server
* ./ngrok http 5000

change Url
* http://localhost:5000 -> https://d9233c34.ngrok.io in templates/Dog-Cat-Classifier.html

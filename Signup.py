from flask import Flask, abort, request 
import json

app = Flask(__name__)

#Custom funtion for errors
@app.errorhandler(404)
def not_found(error=None):
    message = {
            'status':'false',
            'statuscode': 400,
            'message': 'Not Found: ' + request.url,
    }
    resp = json.dumps(message)

    return resp

#Custom funtion for missing parameter
def missing_parameter(key,message):
    message = {
            'status':'false',
            'statuscode': 404,
            'message': key + ' ' + message,
    }
    resp = json.dumps(message)

    return resp


#Custom funtion for checking key for POST request
def check_key_for_POST(param_key):
    if param_key in request.form:
        return True
    else:
        return False

#Custom funtion for checking key for GET request
def check_key_for_GET(param_key):
    username = request.args.get('username', '')
    if username != '':
        return True
    else:
        return False

#Funtion for signup request
@app.route('/DEMO/api/v1/signup', methods=['POST']) 
def signup():
    #input_json = request.get_json(force=True)
    if check_key_for_POST('name'):
        name = request.form['name']
        return json.dumps({'status':'true','name':name})
    else:
        return missing_parameter('name','key is not present.')



#Funtion for login request
@app.route('/DEMO/api/v1/login', methods=['GET']) 
def login():
    username = request.args.get('username', '')
    if username != '':
        return json.dumps({'status':'true','username':username})
    else:
        return missing_parameter('username','key is not present or empty.')

if __name__ == '__main__':
    app.run(host='192.168.1.4', port=8000, debug=True)
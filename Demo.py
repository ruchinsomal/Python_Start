from flask import Flask, abort, request 
import json
from flaskext.mysql import MySQL
 
mysql = MySQL()
app = Flask(__name__)
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = '1122'
app.config['MYSQL_DATABASE_DB'] = 'DEMO'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

#Custom funtion for errors
@app.errorhandler(404)
def not_found(error=None):
    message = {
            'status':False,
            'statuscode': 400,
            'message': 'Not Found: ' + request.url,
    }
    resp = json.dumps(message)

    return resp

#Custom funtion for missing parameter
def missing_parameter(key,message):
    message = {
            'status':False,
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


def authenticate(username,password):
    cursor = mysql.connect().cursor()
    cursor.execute("SELECT * from signup where email='" + username + "' and password='" + password + "'")
    data = cursor.fetchone()
    #print 'data'+data
    if data is None:
        return False
    else:
        return True


def insert_value_to_database():
    connection = mysql.connect()
    cursor = connection.cursor()
    # cursor.execute("SELECT * from User where Username='" + username + "' and Password='" + password + "'")
    # query = "CREATE TABLE potlala (id INT NOT NULL PRIMARY KEY, name  VARCHAR(40), email VARCHAR(40))"
    query = "INSERT INTO signup (id, name, email, password) VALUES ('123123', 'Maria',  'mariaz@activestate.com', 'qwerty')"
    cursor.execute(query)
    connection.commit()
    #return "123"

#Funtion for signup request
@app.route('/DEMO/api/v1/signup', methods=['POST']) 
def signup():
    #input_json = request.get_json(force=True)
    if check_key_for_POST('name'):
        name = request.form['name']
        insert_value_to_database()
        return json.dumps({'status':True,'name':name})
    else:
        return missing_parameter('name','key is not present.')



#Funtion for login request
@app.route('/DEMO/api/v1/login', methods=['GET']) 
def login():
    username = request.args.get('username', '')
    password = request.args.get('password', '')
    if username != '':
        if password != '':
            if authenticate(username,password):
                return json.dumps({'status':True,'username':username,'password':password})
            else:
                return json.dumps({
            'status':'false',
            'statuscode': 200,
            'message': "Username or password is wrong.",
    })
        else:
            return missing_parameter('password','key is not present or empty.')
    else:
        return missing_parameter('username','key is not present or empty.')

if __name__ == '__main__':
    app.run(host='localhost', port=8000, debug=True)
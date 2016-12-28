from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/createcm', methods=['get'])
def create_cm():
    name = request.args.get('name', "No data") # use default value repalce 'None'
    password = request.args.get('password', "No data")
    # do something, eg. return json response
    return jsonify({'name': name, 'password': password})


if __name__ == '__main__':
    app.run(host='192.168.1.2', port=5000, debug=True)
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/sampleurl', methods = ['get'])
def samplefunction():
    required_params = ['name', 'age']
    missing_params = [key for key in required_params if key not in request.args.keys()]

    if len(missing_params)==0:
        data = {
                "status":"success",
                "name": request.args['name'],
                "age": request.args['age']
               }

        return jsonify(data)
    else:
         resp = {
                 "status":"failure",
                 "error" : "missing parameters",
                 "message" : "Provide %s in request" %(missing_params)
                }
         return jsonify(resp)
         
    if request.args['name']=="":
        resp = {
                 "status":"failure",
                 "error" : "missing value",
                 "message" : "Provide name in request" #%(request.args['name'])
                }
        return jsonify(resp)

if __name__ == '__main__':
    app.run(host='192.168.1.2', port=8080, debug=True)
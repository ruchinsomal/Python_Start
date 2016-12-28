from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
	return "hello world"

@app.route('/yoo/<name>')
def by(name):
	return "hello {}".format(name)

if __name__ == "__main__":
	app.run('0.0.0.0',port=5000)
from flask import Flask, make_response

app = Flask(__name__)

@app.route('/')
def index():
	return "hello world"

@app.route('/keyboard')
def keyboard():
	data = {
		"type":"buttons",
		"buttons": [
			"버튼1", "버튼2", "버튼3"
		]
	}
	res = jsonify(data)
	return res

def jsonify(obj):
	js = json.dumps(obj)
	res = make_response(js)
	res.headers['Content-Type'] = 'application/json'
	return res
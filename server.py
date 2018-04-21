from flask import Flask, make_response, request
import json

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

@app.route('/message', methods=['POSTS'])
def message():
	data = request.json
	rs = {
		'text': data['content']
	}
	return jsonify(rs)
	
def jsonify(obj):
	js = json.dumps(obj, ensure_ascii=False)
	res = make_response(js)
	res.headers['Content-Type'] = 'application/json'
	return res
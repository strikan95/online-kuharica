from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)

app.config.from_object(__name__)

CORS(app, resources={r"/*":{'origins':'http://localhost:8080',
                        "allow_headers":"Access-Control-Allow-Origin"}})

@app.route('/', methods=['GET'])
def index():
    return "<h1>Index</h1>"


@app.route('/hello', methods=['GET'])
def shark():
    return "Hello World"

app.run(debug=True)
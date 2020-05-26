# coding: utf-8
from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin

from app_dir.utils import *

app = Flask(__name__)
CORS(app, support_credentials=True)

app.config['Secret'] = "Secret"

@app.route('/', methods=['GET']) # To prevent Cors issues
@cross_origin(supports_credentials=True)
def index():
    # Sent in GET requests
    response = core(
        request.args.get('amount'),
        request.args.get('from'),
        request.args.get('to')
    )
    # Build the response
    # Let's allow all Origin requests
    response.headers.add('Access-Control-Allow-Origin', '*') # To prevent Cors issues
    return response

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, use_reloader=True)

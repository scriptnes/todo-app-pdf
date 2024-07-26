# -*- coding: utf-8 -*-

from flask import Flask, jsonify, send_from_directory
from dotenv import load_dotenv
import os

# Зареждане на променливите от .env файла
load_dotenv()

app = Flask(__name__, static_folder='static')

@app.route('/config')
def get_config():
    server_url = os.getenv('REACT_APP_SERVER_URL', 'http://localhost:5000')
    return jsonify({'serverUrl': server_url})

@app.route('/')
@app.route('/<path:path>')
def serve_static(path='index.html'):
    if path != "" and os.path.exists(app.static_folder + '/' + path):
        return send_from_directory(app.static_folder, path)
    else:
        return send_from_directory('.', 'index.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=3000)

# wsgi.py
from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World !!"

PRODUCTS = {
    1: { 'id': 1, 'name': 'Skello' },
    2: { 'id': 2, 'name': 'Socialive.tv' },
    3: { 'id': 3, 'name': 'Le Wagon'}
}

@app.route('/api/v1/products')
def products():
    return jsonify(PRODUCTS)


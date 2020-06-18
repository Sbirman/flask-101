# wsgi.py
from flask import Flask, jsonify, abort, request
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

@app.route('/api/v1/products/<int:id>', methods=['GET'])
def one_product(id):
    other_product = PRODUCTS.get(id)
    if other_product is None:
        return abort(404)
    else:
        return PRODUCTS.get(id)

@app.route('/api/v1/products/<int:id>', methods=['DELETE'])
def def_product(id):
    other_product = PRODUCTS.get(id)
    if other_product is None:
        return abort(404)
    else:
        del PRODUCTS[id]
        return '', 201

@app.route('/api/v1/products/', methods=['POST'])
def def_product_add():
    produit = request.get_json()
    PRODUCTS[produit['id']] = produit
    return '', 201

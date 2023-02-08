from flask import Flask, jsonify, request
from products import Products

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hellow World'


@app.route('/products')
def get_products():
    return jsonify({"Products": Products, "Message": "Products´s List"})


@app.route('/products/<string:product_name>')
def get_product(product_name):
    product_found = [product for product in Products if product['name'] == product_name]
    if len(product_found) > 0:
        return jsonify({"Product": product_found[0]})
    else:
        return jsonify({"Message": "product not found"})


@app.route('/products', methods=['POST'])
def add():
    new_product = {
            "name": request.json['name'],
            "value": request.json['value'],
            "quantity": request.json['quantity']
    }
    Products.append(new_product)
    return jsonify({"Message": "product added successfully", "Products": Products})


@app.route('/products/<string:product_name>', methods=['PUT'])
def actualize(product_name):
    product_found = [product for product in Products if product['name'] == product_name]
    if len(product_found) > 0:
        product_found[0]['Name'] = request.json['name']
        product_found[0]['value'] = request.json['value']
        product_found[0]['quantity'] = request.json['quantity']
        return jsonify({
            "Message": "product updated successfully",
            "Products": product_found[0]
        })
    else:
        return jsonify({"Message": "Product not found"})


@app.route('/products/<string:product_name>', methods=['DELETE'])
def delete(product_name):
    product_found = [product for product in Products if product['name'] == product_name]
    if len(product_found) > 0:
        Products.remove(product_found[0])
        return jsonify({
            "Message": "Product deleted successfully",
            "product": Products
            })
    else:
        return jsonify({"Message": "Product not found"})


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)

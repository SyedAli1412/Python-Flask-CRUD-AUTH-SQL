from flask import jsonify, make_response, request
from app import app
from app.services.product_service import ProductService
from app.schemas.product_schema import ProductSchema
from flask import Blueprint

product_schema = ProductSchema()



product_blueprint = Blueprint('product', __name__)

@app.route('/products', methods=['GET'])
def get_all_products():
    try:
        products = ProductService.get_all_products()
        result = product_schema.dump(products, many=True)
        return make_response(jsonify({"products": result}))
    except Exception as e:
        return make_response(jsonify({"error": str(e)}), 500)

@app.route('/products/<id>', methods=['GET'])
def get_product_by_id(id):
    try:
        product = ProductService.get_product_by_id(id)
        if product is None:
            return make_response(jsonify({'error':'Product not found'}), 404)
        result = product_schema.dump(product)
        return make_response(jsonify({"product": result}))
    except Exception as e:
        return make_response(jsonify({"error": str(e)}), 500)

@app.route('/products', methods=['POST'])
def create_product():
    try:
        data = request.get_json()

        errors = product_schema.validate(data)
        if errors:
            return make_response(jsonify(errors), 400)

        product = ProductService.create_product(data)
        result = product_schema.dump(product)
        return make_response(jsonify({"product": result}), 201)
    except Exception as e:
        return make_response(jsonify({"error": str(e)}), 500)

@app.route('/products/<id>', methods=['PUT'])
def update_product_by_id(id):
    try:
        data = request.get_json()
        product = ProductService.get_product_by_id(id)
        if product is None:
            return make_response(jsonify({'error': 'Product not found'}), 404)
        errors = product_schema.validate(data)
        if errors:
            return make_response(jsonify(errors), 400)
        updated_product = ProductService.update_product(product, data)
        result = product_schema.dump(updated_product)
        return make_response(jsonify({"product": result}))
    except Exception as e:
        return make_response(jsonify({"error": str(e)}), 500)

@app.route('/products/<id>', methods=['DELETE'])
def delete_product_by_id(id):
    try:
        product = ProductService.get_product_by_id(id)
        ProductService.delete_product(product)
        return make_response("", 204)
    except Exception as e:
        return make_response(jsonify({"error": str(e)}), 500)

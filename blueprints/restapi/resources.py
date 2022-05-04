from flask import jsonify
from flask_restful import Resource
from blueprints.models import Products


class ProductResource(Resource):
    def get(self):
        products = Products.query.all()
        return jsonify([
            product.to_dict()
            for product in products
        ])


class ProductItemResource(Resource):
    def get(self, product_id):
        print("id =>>", product_id)
        return 'ok'

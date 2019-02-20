from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.item import ItemModel


# inheritance
class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        "price", type=float, required=True, help="This field cannot be left blank!"
    )
    parser.add_argument(
        "store_id", type=int, required=True, help="Every item needs a store id."
    )

    @jwt_required()
    def get(self, name):
        item = ItemModel.find_by_name(name)

        if item:
            return item.json(), 200
        return {"message": "Item not found"}, 404

    @jwt_required()
    def post(self, name):
        item = ItemModel.find_by_name(name)
        if item is None:
            # if item not in db
            data = Item.parser.parse_args()
            item = ItemModel(name, **data)
            try:
                item.save_to_db()
                return {"name": name, "price": data["price"]}, 201
            except:
                return {"message": "something went wrong inserting the item"}, 500
        return {"Message": "An item with name {} already exists".format(name)}, 400

    @jwt_required()
    def delete(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            try:
                item.delete_from_db()
            except:
                return {"message": "something went wrong with deleting the item"}, 500
        return {"message": "{} was deleted".format(name)}, 200

    @jwt_required()
    def put(self, name):
        data = Item.parser.parse_args()
        item = ItemModel.find_by_name(name)

        if item is None:
            item = ItemModel(name, **data)
        else:
            item.price = data["price"]
        try:
            item.save_to_db()
            return item.json(), 201
        except:
            return {"message": "Something went wrong with saving the item"}, 500


class Items(Resource):
    def get(self):
        return {"items": [item.json() for item in ItemModel.query.all()]}

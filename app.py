from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identity
from resources.user import UserRegister
from resources.items import Items, Item
from resources.store import Store, StoreList

app = Flask(__name__)
# location of db, /// means local path
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
# if True it will track everything that changes in the objects
# it does not change the sqlalchemy track but does change the extension
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.secret_key = "Kaleb"
api = Api(app)


jwt = JWT(app, authenticate, identity)  # creates a new endpoint called '/auth'

api.add_resource(Item, "/item/<string:name>")
api.add_resource(Items, "/items/")
api.add_resource(UserRegister, "/register")
api.add_resource(Store, "/store/<string:name>")
api.add_resource(StoreList, "/stores")

# this is so that if we import from this file it would auto kick up the server
if __name__ == "__main__":
    from db import db

    db.init_app(app)
    app.run(port=5000, debug=True)

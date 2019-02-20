from db import db

# extend db.model, then tell it the table where they will be stored
class ItemModel(db.Model):
    __tablename__ = "items"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    price = db.Column(db.Float(precision=2))

    store_id = db.Column(db.Integer, db.ForeignKey("stores.id"))
    store = db.relationship("StoreModel")

    def __init__(self, name, price, store_id):
        self.name = name
        self.price = price
        self.store_id = store_id

    def json(self):
        return {"name": self.name, "price": self.price}

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(
            name=name
        ).first()  # SELECT * FROM items WHERE name=name LIMIT 1

    def save_to_db(self):
        # session is collection of object to be added to the db
        # adding self because it's an object model
        db.session.add(self)
        db.session.commit()
        # this can also be used for updates if the object is changed

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()


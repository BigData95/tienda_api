from .. import db


class Product(db.Model):
    """ Product class model """
    __tablename__ = "products"
    sku = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(100), unique=True)
    description = db.Column(db.Text())
    list_price = db.Column(db.Float())

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class Store(db.Model):
    """ Store class model """
    __tablename__ = "stores"
    store_id = db.Column(db.Integer, primary_key=True)
    store_name = db.Column(db.String(100), unique=True)
    phone = db.Column(db.String(20))
    email = db.Column(db.String(50))
    street = db.Column(db.String(100))
    city = db.Column(db.String(50))
    state = db.Column(db.String(50))

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class Stock(db.Model):
    """ Stock class model """
    __tablename__ = "stocks"
    _id = db.Column(db.Integer, primary_key=True)
    store_name = db.Column(db.Integer, db.ForeignKey('stores.store_name'))
    product_name = db.Column(db.Integer, db.ForeignKey('products.product_name'))
    quantity = db.Column(db.Integer)


    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

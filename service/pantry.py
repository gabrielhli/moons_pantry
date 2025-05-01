# Imports
import pymongo
import configparser
import datetime
from bson import ObjectId
import pymongo.synchronous
import pymongo.synchronous.collection
import pymongo.synchronous.database


class Item:
    # Class representation of a pantry item. Class properties include:
    #   - _id: MongoDB ID
    #   - name: Name of item
    #   - quantity: Quantity of item
    #   - expiration_dt: Expiration Date of item

    _id: ObjectId
    client_conn: pymongo.MongoClient  # client connection using pymongo
    db_conn: pymongo.synchronous.database.Database # database connection using pymongo
    item_conn: pymongo.synchronous.collection.Collection # collection connection using pymongo

    def __init__(self, name: str, quantity: int, expiration_dt: datetime):
        """Constructor for item class"""
        self.name = name
        self.quantity = quantity
        self.expiration_dt = expiration_dt

    def __str__(self):
        """str override"""
        print(f"{self._id}: {self.name} - {self.quantity} (expires @ {self.expiration_dt})")

    @classmethod
    def db_init(cls, db_name = 'Pantry'):
        """ Initializes connection to the Mongodb"""
        config = configparser.ConfigParser()
        config.read('config.ini')
        uri = config.get('database', 'uri')

        try:
            cls.client_conn = pymongo.MongoClient(uri)
            cls.db_conn = cls.client_conn[db_name]
        except ConnectionError:
            print("Unable to connect to MongoDB")

    @classmethod
    def db_close(cls):
        """ Closes connection to Mongodb"""
        cls.client_conn.close()

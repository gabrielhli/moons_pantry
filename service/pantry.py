# Imports
import pymongo
import configparser
import datetime
from bson import ObjectId


class Item:
    # Class representation of a pantry item. Class properties include:
    #   - _id: MongoDB ID
    #   - name: Name of item
    #   - quantity: Quantity of item
    #   - expiration_dt: Expiration Date of item

    _id: ObjectId
    db_conn: pymongo.MongoClient  # db connection using pymongo

    def __init__(self, name: str, quantity: int, expiration_dt: datetime):
        """Constructor for item class"""
        self.name = name
        self.quantity = quantity
        self.expiration_dt = expiration_dt

    def __str__(self):
        """str override"""
        print(f"{self._id}: {self.name} - {self.quantity} (expires @ {self.expiration_dt})")

    @classmethod
    def db_init(self):
        """ Initializes connection to the Mongodb"""
        config = configparser.ConfigParser()
        config.read('config.ini')
        uri = config.get('database', 'uri')

        try:
            self.db_conn = pymongo.MongoClient(uri)
        except ConnectionError:
            print("Unable to connect to MongoDB")

    @classmethod
    def db_close(self):
        """ Closes connection to Mongodb"""
        self.db_conn.close()

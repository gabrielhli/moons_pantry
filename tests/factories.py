"""
Test Factory to make fake objects for testing
"""
from datetime import date
import factory
from factory.fuzzy import FuzzyDate, FuzzyInteger
from service.pantry import Item

class ItemFactory(factory.Factory):
    """ Creates fake Items"""
    class Meta:
        """ Persistent class for factory"""
        model = Item

    name = factory.Faker("name")
    quantity = FuzzyInteger(0, 100)
    expiration_dt = FuzzyDate(date(2025,1,1))
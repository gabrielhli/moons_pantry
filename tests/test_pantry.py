"""
Test file for testing pantry.py
"""
import pytest
import logging
from service import pantry
from tests.factories import ItemFactory


class TestPantry:
    """ Main Test Class """

    # Setting up logger
    logging.basicConfig(filename="TestPantry.log",
                        format='%(asctime)s %(message)s',
                        filemode='w')
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    @pytest.fixture(autouse=True, scope="class")
    def setup_method(self):
        """ Class fixture for setup and teardown."""

        # Class Setup
        pantry.Item.db_init("test-db")
        print("setup")
        self.logger.debug("setup")
        yield

        # Class Teardown
        pantry.Item.db_close()
        print("teardown")
        self.logger.debug("teardown")

    @pytest.fixture(autouse=True, scope="function")
    def test_method(self):
        """ function fixture for setup and teardown before each test."""

        # Test setup
        self.logger.debug("test setup")
        yield

        # Test teardown
        self.logger.debug("test teardown")

    def test_str_function(self):
        """ Tests the __str__ function of Item"""
        item = ItemFactory()
        self.logger.debug(item.name)
        self.logger.debug(item.quantity)
        self.logger.debug(item.expiration_dt)
        assert f"{item.name}: {item.quantity} - {item.expiration_dt}" == item.__str__()

    def test_sample2(self):
        assert 10 != 5

    def test_create_item(self):
        """ Tests the create_item function """
        origCount = pantry.Item.count()
        item = ItemFactory()
        self.logger.debug("Testing create item with the following attributes")
        self.logger.debug(item.name)
        self.logger.debug(item.quantity)
        self.logger.debug(item.expiration_dt)
        item.createItem()
        assert origCount + 1 == pantry.Item.count()

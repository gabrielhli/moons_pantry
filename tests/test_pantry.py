# Imports
import pytest
from service import pantry


@pytest.fixture(scope="module")
def init_db():
    pantry.Item.db_init()


def test_sample():
    assert 5 == 5

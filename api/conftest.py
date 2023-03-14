import pytest
import configparser
from item.item_test_helper import ItemTestHelper

@pytest.fixture(scope='session')
def sut_addr():
    config = configparser.ConfigParser()
    config.read('./api/SUT.ini')
    assert 'HOST' in config
    assert 'SERVER_IP' in config['HOST']
    assert 'PORT' in config['HOST']
    return f"http://{config['HOST']['SERVER_IP']}:{config['HOST']['PORT']}"

@pytest.fixture(scope='package')
def item_test_helper(sut_addr):
    return ItemTestHelper(sut_addr)
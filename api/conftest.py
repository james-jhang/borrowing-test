import pytest
import configparser
from item.item_test_helper import ItemTestHelper
from user.user_test_helper import UserTestHelper
from custodian.custodian_test_helper import CustodianTestHelper

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

@pytest.fixture(scope='package')
def user_test_helper(sut_addr):
    return UserTestHelper(sut_addr)

@pytest.fixture(scope='package')
def custodian_test_helper(sut_addr):
    return CustodianTestHelper(sut_addr)
from custodian.custodian_test_helper import CustodianTestHelper

class TestRegisterCustodian:

    def test_register_a_custodian(self, custodian_test_helper: CustodianTestHelper):
        custodian = {
            'name': 'James Jhang'
        }
        registered_custodian = custodian_test_helper.register(custodian)
        assert registered_custodian['name'] == 'James Jhang'
        assert 'id' in registered_custodian
        assert registered_custodian['id'] != None
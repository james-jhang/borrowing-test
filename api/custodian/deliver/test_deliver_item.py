from custodian.custodian_test_helper import CustodianTestHelper
from user.user_test_helper import UserTestHelper
from item.item_test_helper import ItemTestHelper

class TestDeliverItem:
    def test_deliver_a_reservation(self, 
                                   custodian_test_helper: CustodianTestHelper,
                                   user_test_helper: UserTestHelper,
                                   item_test_helper: ItemTestHelper):
        item = item_test_helper.create_an_item({'name': 'Table'})
        user = user_test_helper.register({'name': 'Olivia'})
        custodian = custodian_test_helper.register({'name': 'James'})
        reservation = user_test_helper.reserve(
            user, item, "2023/03/01", "2023/03/10"
        )
        IOU = custodian_test_helper.deliver(
            custodian, user, reservation
        )
        assert 'iouid' in IOU
        assert IOU['iouid'] != None
        assert IOU['custodianID'] == custodian['custodianID']
        assert IOU['userID'] == user['userID']
        assert IOU['itemID'] == item['itemID']
        assert IOU['startDate'] == "2023/03/01"
        assert IOU['endDate'] == "2023/03/10"

        item_test_helper.delete_item(item['itemID'])
        # TODO implement the teardown of all test cases


        
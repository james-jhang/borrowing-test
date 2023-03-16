from user.user_test_helper import UserTestHelper
from item.item_test_helper import ItemTestHelper

class TestReserveItem:

    def test_reserve_an_item(self, user_test_helper: UserTestHelper, item_test_helper: ItemTestHelper):
        user = {
            'name': 'Olivia'
        }
        item = {
            'name': 'Pen'
        }
        ruser = user_test_helper.register(user)
        citem = item_test_helper.create_an_item(item)
        reservation = user_test_helper.reserve(
            ruser, citem, "2022/01/01", "2022/01/03"
        )

        assert 'id' in reservation
        assert reservation['id'] != None
        assert reservation['userID'] == ruser['id']
        assert reservation['itemID'] == citem['id']
        assert reservation['startDate'] == "2022/01/01"
        assert reservation['endDate'] == "2022/01/03"
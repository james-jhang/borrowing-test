from user.member.member_test_helper import MemberTestHelper
from item.item_test_helper import ItemTestHelper

class TestReserveItem:

    def test_reserve_an_item(self, member_test_helper: MemberTestHelper, item_test_helper: ItemTestHelper):
        member = {
            'name': 'Olivia'
        }
        item = {
            'name': 'Pen'
        }
        rmember = member_test_helper.register(member)
        citem = item_test_helper.create_an_item(item)
        reservation = member_test_helper.reserve(rmember, citem)
        
        assert reservation['userID'] == rmember['id']
        assert reservation['itemID'] == citem['id']
        assert 'id' in reservation
        assert reservation['id'] != None
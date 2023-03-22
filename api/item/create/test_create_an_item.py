from item.item_test_helper import ItemTestHelper

class TestCreateAnItem:

    def test_create_an_item(self, item_test_helper: ItemTestHelper):
        item = {
            'name': '等身立鏡'
        }
        created_item = item_test_helper.create_an_item(item)
        assert '等身立鏡' == created_item['name']
        assert 'itemID' in created_item
        assert None != created_item['itemID']

        item_test_helper.delete_item(created_item['itemID'])
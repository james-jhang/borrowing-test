import pytest
from item.item_test_helper import ItemTestHelper

class TestDeleteItem:
    def test_delete_an_item(self, item_test_helper: ItemTestHelper):
        eraser = item_test_helper.create_an_item({
            'name': '板擦'
        })
        rag = item_test_helper.create_an_item({
            'name': '抹布'
        })
        item_test_helper.delete_item(eraser['itemID'])
        items = item_test_helper.list_all_items()
        assert len(items) == 1
        self.__the_eraser_should_not_be_in_the_list(eraser, items)
        item_test_helper.delete_item(rag['itemID'])
        items = item_test_helper.list_all_items()
        assert len(items) == 0
        
    def __the_eraser_should_not_be_in_the_list(self, eraser, items):
        for item in items:
            if eraser['itemID'] == item['itemID']:
                pytest.fail("The deleted item should not be in the item list.")
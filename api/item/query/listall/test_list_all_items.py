from item.item_test_helper import ItemTestHelper

class TestListAllItems:

    def test_list_all_items(self, item_test_helper: ItemTestHelper):
        eraser = item_test_helper.create_an_item({
            'name': '板擦'
        })
        rag = item_test_helper.create_an_item({
            'name': '抹布'
        })
        item_list = item_test_helper.list_all_items()
        assert len(item_list) == 2
        self.__the_list_should_contain_items(item_list, eraser, rag)

        item_test_helper.delete_item(eraser['itemID'])
        item_test_helper.delete_item(rag['itemID'])

    def __the_list_should_contain_items(self, item_list, *items):
        item_ids = list(map(lambda item: item['itemID'], item_list))
        for item in items:
            assert item['itemID'] in item_ids
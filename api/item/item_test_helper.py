import requests

class ItemTestHelper:
    def __init__(self, sut_addr):
        self.sut_addr = sut_addr

    def create_an_item(self, item_data):
        return requests.post(
            url=self.sut_addr+'/api/items/create',
            json=item_data
        ).json()
    
    def delete_item(self, item_id):
        return requests.delete(
            url=self.sut_addr+'/api/items',
            params={'id': item_id}
        )
    
    def list_all_items(self):
        return requests.get(
            url=self.sut_addr+'/api/items/list'
        ).json()
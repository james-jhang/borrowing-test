import requests

class MemberTestHelper:
    def __init__(self, sut_addr):
        self.sut_addr = sut_addr

    def register(self, member_data):
        return requests.post(
            url=self.sut_addr+'/api/members/register',
            json=member_data
        ).json()
    
    def delete(self, member_id):
        # TODO there has not an api for deleting members yet.
        return requests.delete(
            url=self.sut_addr+'/api/members',
            params={'id': member_id}
        )
    
    def reserve(self, user, item):
        return requests.post(
            url=self.sut_addr+'/api/members/reserve',
            json={
                'userID': user['id'],
                'itemID': item['id']
            }
        ).json()
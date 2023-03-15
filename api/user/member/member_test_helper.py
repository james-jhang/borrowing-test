import requests

class MemberTestHelper:
    def __init__(self, sut_addr):
        self.sut_addr = sut_addr

    def register(self, member_data):
        return requests.post(
            url=self.sut_addr+'/api/users/register',
            json=member_data
        ).json()
    
    def delete(self, member_id):
        return requests.delete(
            url=self.sut_addr+'/api/users',
            params={'id': member_id}
        )
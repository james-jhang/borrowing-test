import requests

class UserTestHelper:
    def __init__(self, sut_addr):
        self.sut_addr = sut_addr

    # TODO passing value is better than passing json data
    def register(self, user_data):
        return requests.post(
            url=self.sut_addr+'/api/users/register',
            json=user_data
        ).json()
    
    def delete(self, user_id):
        # TODO there has not an api for deleting users yet.
        return requests.delete(
            url=self.sut_addr+'/api/users',
            params={'id': user_id}
        )
    
    def reserve(self, user, item, start_date, end_date):
        return requests.post(
            url=self.sut_addr+'/api/users/reserve',
            json={
                'userID': user['userID'],
                'itemID': item['itemID'],
                'startDate': start_date,
                'endDate': end_date
            }
        ).json()
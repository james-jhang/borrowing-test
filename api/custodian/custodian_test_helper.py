import requests

class CustodianTestHelper:

    def __init__(self, sut_addr):
        self.sut_addr = sut_addr

    def register(self, custodian_data):
        return requests.post(
            url=self.sut_addr+'/api/custodians/register',
            json=custodian_data
        ).json()
    
    def deliver(self, custodian, user, reservation):
        return requests.post(
            url=self.sut_addr + '/api/custodians/deliver',
            json={
                'custodianID': custodian['custodianID'],
                'userID': user['userID'],
                'reservationID': reservation['reservationID']
            }
        ).json()
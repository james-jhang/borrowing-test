from user.user_test_helper import UserTestHelper

class TestRegisterUser:

    def test_register_a_user(self, user_test_helper: UserTestHelper):
        user = {
            'name': 'James'
        }
        registered_user = user_test_helper.register(user)
        assert registered_user['name'] == 'James'
        assert 'id' in registered_user
        assert registered_user['id'] != None

        user_test_helper.delete(registered_user['id'])

from user.member.member_test_helper import MemberTestHelper

class TestRegisterMember:

    def test_register_a_member(self, member_test_helper: MemberTestHelper):
        member = {
            'name': 'James'
        }
        registered_member = member_test_helper.register(member)
        assert registered_member['name'] == 'James'
        assert 'id' in registered_member
        assert registered_member['id'] != None

        member_test_helper.delete(registered_member['id'])

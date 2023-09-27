from src.assertions import Assertion
from src.create_user import CreateUser
from src.my_requests import MyRequests
from data.status_code import StatusCode
from src.update_user import UpdateUser


class TestUpdateUsers:
    assertion = Assertion()
    status_code = StatusCode()
    put_method = UpdateUser()

    def test_update_user(self, make_user):
        user_id = make_user.json()["user_id"]
        response = self.put_method.update_user_with_valid_data(user_id)
        self.assertion.assert_status_code(response, self.status_code.OK)

    def test_update_first_name(self, make_user):
        response, first_name = self.put_method.update_first_name(make_user)
        self.assertion.assert_that_text_not_equal(response.json()["first_name"], first_name)


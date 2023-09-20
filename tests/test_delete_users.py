from src.create_user import CreateUser
from src.delete_user import DeleteUser
from src.my_requests import MyRequests
from src.assertions import Assertion
from data.status_code import StatusCode


class TestDeleteUsers:
    assertion = Assertion()
    status_code = StatusCode()

    def test_delete_users(self, make_user):
        delete_method = DeleteUser()
        response = delete_method.delete_user(make_user)
        self.assertion.assert_status_code(response, self.status_code.ACTUAL)

    def test_delete_users_has_text_null(self):
        response = MyRequests.delete("/users/22159")
        actual_text = response.text
        self.assertion.assert_text(actual_text, "null")

    def test_delete_deleted_users_has_status_code_404(self):
        response = MyRequests.delete("/users/21882")
        self.assertion.assert_status_code(response, self.status_code.NOT_FOUND)

    def test_delete_deleted_users_has_text(self):
        response = MyRequests.delete("/users/21882")
        actual_text = response.json()["detail"]["reason"]
        self.assertion.assert_text(actual_text, "User with requested id: 21882 is absent")


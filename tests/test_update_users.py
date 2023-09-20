from src.assertions import Assertion
from src.create_user import CreateUser
from src.my_requests import MyRequests
from data.status_code import StatusCode
from src.update_user import UpdateUser


class TestUpdateUsers:
    assertion = Assertion()
    status_code = StatusCode()
    body = {
        "first_name": "David",
        "last_name": "David",
        "company_id": 1
    }

    def test_update_user(self):
        response = MyRequests.put("/users/21899", self.body)
        assert response.json()["first_name"] != "Denis", "First name was not updated"
        assert response.json()["last_name"] != "Denis", "Last name was not updated"
        self.assertion.assert_status_code(response, self.status_code.OK)

    def test_update_first_name(self, make_user):
        put_method = UpdateUser()
        response, first_name = put_method.update_first_name(make_user)
        assert response.json()["first_name"] != first_name


from src.assertions import Assertion
from src.my_requests import MyRequests
from data.status_code import StatusCode


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
        print(response.json())
        assert response.json()["first_name"] != "Denis", "First name was not updated"
        assert response.json()["last_name"] != "Denis", "Last name was not updated"
        self.assertion.assert_status_code(response, self.status_code.OK)

from src.my_requests import MyRequests


class TestUpdateUsers:
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
        assert response.status_code == 200, f"Status code not 200, status code is {response.status_code}"

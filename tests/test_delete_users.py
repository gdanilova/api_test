from src.my_requests import MyRequests


class TestDeleteUsers:

    def test_delete_users(self):
        response = MyRequests.delete("/users/21884")
        print(response.text)
        assert response.status_code == 202, f"Status code not 202, status code is {response.status_code}"

    def test_delete_users_has_text_null(self):
        response = MyRequests.delete("/users/21888")
        assert response.text == "null", "Wrong text"

    def test_delete_deleted_users_has_status_code_404(self):
        response = MyRequests.delete("/users/21882")
        assert response.status_code == 404, f"Status code not 404, status code is {response.status_code}"

    def test_delete_deleted_users_has_text(self):
        response = MyRequests.delete("/users/21882")
        assert response.json()["detail"]["reason"] == "User with requested id: 21882 is absent", "Wrong text"

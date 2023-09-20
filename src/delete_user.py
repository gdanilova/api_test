from data.urls import Urls
from src.base_page import BasePage
from src.my_requests import MyRequests


class DeleteUser(BasePage):
    url = Urls()


    def delete_user(self, response):
        user_id = response.json()["user_id"]
        url = f"{self.url.create_user}{user_id}"
        response = MyRequests.delete(url)
        return response
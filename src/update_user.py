from data.urls import Urls
from generator.generator import generated_person
from src.base_page import BasePage
from src.my_requests import MyRequests


class UpdateUser(BasePage):
    url = Urls()

    def update_first_name(self, response):
        first_name_before, last_name, company_id, user_id = self.get_all_user_values(response)
        person_info = next(generated_person())
        first_name = person_info.first_name
        body = self.prepare_creating_data(first_name=first_name, last_name=last_name, company_id=company_id)
        url = f"{self.url.create_user}{user_id}"
        response = MyRequests.put(url, body)
        return response, first_name_before

    def get_all_user_values(self, response):
        first_name = response.json()["first_name"]
        last_name = response.json()["last_name"]
        company_id = response.json()["company_id"]
        user_id = response.json()["user_id"]
        return first_name, last_name, company_id, user_id

    def update_user_with_valid_data(self, user_id):
        first_name, last_name, company_id = self.get_user_values()
        body = self.prepare_creating_data(first_name=first_name, last_name=last_name, company_id=company_id)
        url = f"{self.url.create_user}{user_id}"
        response = MyRequests.put(url, body)
        return response
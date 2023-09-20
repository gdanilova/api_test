from data.urls import Urls
from generator.generator import generated_person
from src.base_page import BasePage
from src.my_requests import MyRequests


class CreateUser(BasePage):
    url = Urls()

    def create_user_without_first_name(self):
        person_info = next(generated_person())
        last_name = person_info.last_name
        company_id = person_info.company_id
        body = self.prepare_creating_data(last_name=last_name, company_id=company_id)
        response = MyRequests.post(self.url.create_user, body)
        return response, last_name



import random

from data.urls import Urls
from generator.generator import generated_person
from src.my_requests import MyRequests


class BasePage:
    url = Urls()

    def get_user(self, body):
        response = MyRequests.post(self.url.create_user, body)
        return response

    def get_id_company(self, data, active_company):
        values = data[active_company]
        return random.choice(values)

    def create_user_with_invalid_company_id(self, company_id):
        person_info = next(generated_person())
        first_name = person_info.first_name
        last_name = person_info.last_name
        body = {
            "first_name": first_name,
            "last_name": last_name,
            "company_id": company_id
        }
        return body


    def prepare_creating_data(self, first_name=None, last_name=None, company_id=None):
        if first_name is None:
            return {"last_name": last_name,
                    "company_id": company_id
                    }
        if last_name is None:
            return {"first_name": first_name,
                    "company_id": company_id
                    }
        if company_id is None:
            return {"first_name": first_name,
                    "last_name": last_name
                    }
        else:
            return {"first_name": first_name,
                    "last_name": last_name,
                    "company_id": company_id
                    }

    def get_user_values(self):
        person_info = next(generated_person())
        first_name = person_info.first_name
        last_name = person_info.last_name
        company_id = person_info.company_id
        return first_name, last_name, company_id
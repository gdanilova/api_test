from data.urls import Urls
from src.my_requests import MyRequests


class BasePage:
    url = Urls()

    def get_user(self, body):
        response = MyRequests.post(self.url.create_user, body)
        return response

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
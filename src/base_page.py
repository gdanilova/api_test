

class BasePage:

    def get_body(self, first_name, last_name, company_id):
        body = {
            "first_name": first_name,
            "last_name": last_name,
            "company_id": company_id
        }
        return body
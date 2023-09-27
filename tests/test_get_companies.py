import pytest
from src.assertions import Assertion
from src.get_companies import GetCompanies
from data.data_files import StatusCompanies
from src.my_requests import MyRequests


class TestStatusCompanies:
    status_list = StatusCompanies.status_list
    request = MyRequests()
    get_companies = GetCompanies()
    assertion = Assertion()

    def test_get_statuses_companies1(self, read_companies_data):
        data = read_companies_data
        value = self.get_companies.get_id_company(data, "closed")
        print(value)

    @pytest.mark.parametrize("status", status_list)
    def test_get_statuses_companies(self, status):
        response = self.request.get(f"/companies/?status={status}&limit=3&offset=0")
        self.assertion.assert_status_code(response, 200)

    @pytest.mark.parametrize("status", status_list)
    def test_get_closed_companies(self, status):
        response = self.request.get(f"/companies/?status={status}&limit=3&offset=0")
        items_list = response.json()["data"]
        for item in items_list:
            self.assertion.assert_text(item["company_status"], status)

    # def test_get_timeout(self):
    #     response = self.request.get(f"/companies/?status=ACTIVE&limit=3&offset=0")
    #     print(response.elapsed.total_seconds())

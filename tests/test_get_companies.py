from pprint import pprint

import pytest
import requests

from data.data_files import StatusCompanies
from src.my_requests import MyRequests


class TestStatusCompanies:
    status_list = StatusCompanies.status_list
    request = MyRequests()

    @pytest.mark.parametrize("status", status_list)
    def test_get_statuses_companies(self, status):
        response = self.request.get(f"/companies/?status={status}&limit=3&offset=0")
        # print()
        # pprint(response.json())
        assert response.status_code == 200, f"Status code is not 200, status code is {response.status_code}"

    @pytest.mark.parametrize("status", status_list)
    def test_get_closed_companies(self, status):
        response = self.request.get(f"/companies/?status={status}&limit=3&offset=0")
        items_list = response.json()["data"]
        for item in items_list:
            assert item["company_status"] == status

    # def test_get_timeout(self):
    #     response = self.request.get(f"/companies/?status=ACTIVE&limit=3&offset=0")
    #     print(response.elapsed.total_seconds())

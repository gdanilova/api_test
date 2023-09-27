import pytest

from data.data_files import KeysCreateUser, StatusCompanies
from src.create_user import CreateUser
from src.assertions import Assertion
from data.status_code import StatusCode


class TestCreateUsers:
    company_status = StatusCompanies()
    assertion = Assertion()
    status_code = StatusCode()
    keys = KeysCreateUser()
    post_method = CreateUser()

    def test_get_status_code_201(self, prepare_user_in_active_company):
        response = self.post_method.get_user(prepare_user_in_active_company)
        self.assertion.assert_status_code(response, self.status_code.CREATE)

    @pytest.mark.parametrize("key", keys.keys)
    def test_check_keys_in_response(self, prepare_user_in_active_company, key):
        self.post_method.get_user(prepare_user_in_active_company)

    def test_create_user_without_first_name(self):
        self.post_method.create_user_without_first_name()
        response, last_name = self.post_method.create_user_without_first_name()
        self.assertion.assert_status_code(response, self.status_code.CREATE)
        self.assertion.assert_first_name(response, None)
        self.assertion.assert_last_name(response, last_name)
    @pytest.mark.parametrize("company_id", company_status.invalid_company_status)
    def test_create_user_from_closed_company(self, read_companies_data, company_id):
        company_id = self.post_method.get_id_company(read_companies_data, "closed")
        body = self.post_method.create_user_with_invalid_company_id(company_id)
        response = self.post_method.get_user(body)
        self.assertion.assert_status_code(response, self.status_code.BAD_REQUEST)
import pytest

from data.data_files import KeysCreateUser
from src.create_user import CreateUser
from src.assertions import Assertion
from data.status_code import StatusCode


class TestCreateUsers:
    assertion = Assertion()
    status_code = StatusCode()
    keys = KeysCreateUser()

    def test_get_status_code_201(self, prepare_user_in_active_company):
        post_method = CreateUser()
        response = post_method.get_user(prepare_user_in_active_company)
        self.assertion.assert_status_code(response, self.status_code.CREATE)

    @pytest.mark.parametrize("key", keys.keys)
    def test_check_keys_in_response(self, prepare_user_in_active_company, key):
        post_method = CreateUser()
        post_method.get_user(prepare_user_in_active_company)

    def test_create_user_without_first_name(self):
        post_method = CreateUser()
        post_method.create_user_without_first_name()
        response, last_name = post_method.create_user_without_first_name()
        self.assertion.assert_status_code(response, self.status_code.CREATE)
        self.assertion.assert_first_name(response, None)
        self.assertion.assert_last_name(response, last_name)
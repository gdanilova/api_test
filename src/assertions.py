import json

import requests
from requests import Response


class Assertion:
    @staticmethod
    def assert_status_code(response: Response, expected_status_code: int):
        actual_status_code = response.status_code
        assert actual_status_code == expected_status_code, \
            f"Unexpected status code. Expected: {expected_status_code}, Actual: {actual_status_code}"

    @staticmethod
    def assert_json_has_key(response: Response, name):
        try:
            response_json = response.json()
        except json.JSONDecodeError:
            assert False, f"""Response is not JSON format. Response text is '{response.text}'"""
        assert name in response_json, f"""response JSON doesn't have key '{name}'"""

    @staticmethod
    def assert_text(actual_text, expected_text):
        assert actual_text == expected_text, "Text is not equal"

    @staticmethod
    def assert_that_text_not_equal(actual_text, expected_text):
        assert actual_text != expected_text, "Text is equal"

    @staticmethod
    def assert_first_name(response: Response, expected_text):
        actual_text = response.json()
        assert actual_text["first_name"] == expected_text

    @staticmethod
    def assert_last_name(response: Response, expected_text):
        actual_text = response.json()
        assert actual_text["last_name"] == expected_text

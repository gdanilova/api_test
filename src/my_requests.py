import requests
from data.urls import base_url


class MyRequests:
    @staticmethod
    def get(url: str, data: dict = None, headers: dict = None, cookies: dict = None):
        response = MyRequests._send(url, data, headers, cookies, "GET")
        return response

    @staticmethod
    def post(url: str, data: dict = None, headers: dict = None, cookies: dict = None):
        response = MyRequests._send(url, data, headers, cookies, "POST")
        return response

    @staticmethod
    def put(url: str, data: dict = None, headers: dict = None, cookies: dict = None):
        response = MyRequests._send(url, data, headers, cookies, "PUT")
        return response

    @staticmethod
    def delete(url: str, data: dict = None, headers: dict = None, cookies: dict = None):
        response = MyRequests._send(url, data, headers, cookies, "DELETE")
        return response

    @staticmethod
    def _send(url: str, data: dict, headers: dict, cookies: dict, method: str):
        url = f"""{base_url}{url}"""

        if headers is None:
            headers = {}
        if cookies is None:
            cookies = {}

        if method == "GET":
            response = requests.get(url, params=data, headers=headers, cookies=cookies)
        elif method == "POST":
            response = requests.post(url, data=data, headers=headers, cookies=cookies)
        elif method == "PUT":
            response = requests.put(url, data=data, headers=headers, cookies=cookies)
        elif method == "DELETE":
            response = requests.delete(url, data=data, headers=headers, cookies=cookies)
        else:
            raise Exception(f"""Bad method {method} was received""")
        return response

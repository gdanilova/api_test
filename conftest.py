import json
import os
import shutil

import pytest
import requests

from data.urls import Urls
from generator.generator import generated_person
from src.create_user import CreateUser


@pytest.fixture(scope="function")
def prepare_user_in_active_company():
    person_info = next(generated_person())
    first_name = person_info.first_name
    last_name = person_info.last_name
    company_id = person_info.company_id
    body = {
        "first_name": first_name,
        "last_name": last_name,
        "company_id": company_id
    }
    return body


@pytest.fixture(scope="session", autouse=True)
def get_all_companies(get_absolute_path):
    response = requests.get(f"{Urls.base_url}/companies/?status=ACTIVE&limit=10000").json()["data"]
    active = [item["company_id"] for item in response]
    response = requests.get(f"{Urls.base_url}/companies/?status=CLOSED&limit=10000").json()["data"]
    closed = [item["company_id"] for item in response]
    response = requests.get(f"{Urls.base_url}/companies/?status=BANKRUPT&limit=10000").json()["data"]
    bankrupt = [item["company_id"] for item in response]
    data = {"active": active, "closed": closed, "bankrupt": bankrupt}
    # Определение абсолютного пути к корневой директории проекта
    root_directory = get_absolute_path
    # Путь к папке json_data в корне проекта
    json_data_directory = os.path.join(root_directory, 'json_data')
    # Создаем папку json_data, если она не существует
    os.makedirs(json_data_directory, exist_ok=True)

    # Путь к файлу JSON внутри папки json_data
    json_file_path = os.path.join(json_data_directory, 'companies_data.json')

    # Сохраняем данные в файл JSON
    with open(json_file_path, 'w') as json_file:
        json.dump(data, json_file)


@pytest.fixture(scope="session")
def get_absolute_path():
    # Путь к папке json_data в корне проекта
    root_directory = os.path.dirname(os.path.abspath(__file__))
    return root_directory

@pytest.fixture()
def make_user(prepare_user_in_active_company):
    post_method = CreateUser()
    response = post_method.get_user(prepare_user_in_active_company)
    return response

@pytest.fixture(scope="function")
def read_companies_data(get_absolute_path):
    root_directory = get_absolute_path
    json_data_directory = os.path.join(root_directory, 'json_data')
    file_name = os.path.join(json_data_directory, 'companies_data.json')
    try:
        with open(file_name, 'r', encoding='utf-8') as json_file:
            json_data = json.load(json_file)
            return json_data
    except FileExistsError:
        print(f"File {file_name} does not exist")
    except json.JSONDecodeError:
        print(f"File {file_name} is not JSON format")


def clear_logs_dir():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    logs_dir = os.path.join(current_dir, "logs")
    if os.path.exists(logs_dir):
        shutil.rmtree(logs_dir)

        os.makedirs(logs_dir, exist_ok=True)
@pytest.hookimpl(tryfirst=True)
def pytest_sessionstart(session):
    clear_logs_dir()
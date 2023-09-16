from data.data import Person
from random import randint
from faker import Faker


faker_eng = Faker("En")
Faker.seed()


def generated_person():
    yield Person(
        first_name=faker_eng.first_name(),
        last_name=faker_eng.last_name(),
        company_id=randint(1, 3)
    )
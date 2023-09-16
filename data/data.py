from dataclasses import dataclass


@dataclass
class Person:
    first_name: str = None
    last_name: str = None
    company_id: int = None

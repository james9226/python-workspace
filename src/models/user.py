from dataclasses import dataclass


@dataclass
class User:
    email: str
    hashed_password: str
    is_enabled: bool
    uuid: str

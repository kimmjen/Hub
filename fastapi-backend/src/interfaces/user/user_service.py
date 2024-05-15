from abc import ABC, abstractmethod


class UserService(ABC):
    @abstractmethod
    def get_user(self, user_id: int) -> dict:
        pass

    @abstractmethod
    def create_user(self, user: dict) -> dict:
        pass

    @abstractmethod
    def update_user(self, user_id: int, user: dict) -> dict:
        pass

    @abstractmethod
    def delete_user(self, user_id: int) -> dict:
        pass

    @abstractmethod
    def get_users(self) -> list:
        pass

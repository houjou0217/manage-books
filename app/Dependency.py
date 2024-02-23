from injector import Binder, Injector
from repository.UserRepository import AbstractUserRepository, UserRepository
from service.UserService import UserService


class Dependency:
    def __init__(self) -> None:
        self.injector = Injector(self.__class__.config)

    @classmethod
    def config(cls, binder: Binder):
        binder.bind(AbstractUserRepository, to=UserRepository)
        binder.bind(UserService, to=UserService)

    def resolve(self, cls):
        return self.injector.get(cls)

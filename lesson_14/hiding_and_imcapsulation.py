from abc import ABC, abstractmethod


class Employee(ABC):
    def __init__(self, salary, position):
        self.salary = salary
        self.position = position

    @abstractmethod
    def do_work(self):
        pass

    def chill(self):
        print("chillin")


class Engineer(Employee):
    def __init__(self):
        super().__init__(4000, "Engineer")


    def _deploy_program(self):
        print("Deploying")


    def __create_framework(self):
        print("Creating new framework")

    def __create_infrastracture(self):
        print("Creating infrastracture")

    def deploy(self):
        self.__create_infrastracture()
        self.__create_framework()
        self._deploy_program()


    def do_work(self):
        print("I`m creating new framework")


class Developer(Engineer):
    def __init__(self):
        super().__init__()

    def do_work(self):
        print("I`m writing new program using framework")
        self._deploy_program
        self.deploy()

developer= Developer()
developer.do_work()

class Human:
    def __init__(self, name, age):
        self.__hidden_name = name
        self._age = age

        @property
        def name(self):





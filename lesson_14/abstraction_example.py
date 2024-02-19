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


class DTEKEmployee(Employee):
    def __init__(self, salary, position):
        super().__init__(salary, position)

    def do_work(self):
        print("I`m welder from DTEK")

mykola = DTEKEmployee(3000, "welder")
mykola.do_work()
mykola.chill()
#employee = Employee(1, "a")

class Car(ABC):
    def __init__(self, color, power):
        self.color = color
        self.power = power
        self.wheels = 4
        self.engin = True
        self.engin_type = None

    def move_forward(self):
        print("I move forward")

    def move_left(self):
        print("I move left")

    def move_rigth(self):
        print("I move right")

    @abstractmethod
    def refuel(self):
        pass

class Toyota(Car):
    def __init__(self, color, power):
        super().__init__(color, power)
        self.engin_type = "DVS"

    def refuel(self):
        print("Refill with gas")

class Tesla(Car):
    def __init__(self, color, power):
        super().__init__(color, power)
        self.engin_type = "Electric"

    def refuel(self):
        print("Plug in the wire")

toyota = Toyota("green", 200)
toyota.refuel()
toyota.move_rigth()

tesla = Tesla("white", 300)
tesla.refuel()
tesla.move_left()

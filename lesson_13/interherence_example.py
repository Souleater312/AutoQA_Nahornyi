class Human:
    def __init__(self,name:str, age:int, gender):
        self.name = name
        self.age = age
        self.gender = gender


class Employee(Human):
    def __init__(self, name, age, gender, job_position, salary):
        super().__init__(name, age, gender)
        self.job_position = job_position
        self.salary = salary


john = Human("John", 30, "male")
evelynn = Employee("Evelynn", 32, "female", "aqa", 4800)

class Donkey:
    strenghy = 5

    @classmethod
    def print_strenghy(cls):
        print(cls, cls.strenghy)


class Horse:
    speed = 10


    @classmethod
    def print_strenghy(cls):
        print(cls, cls.strenghy)


class Mul(Horse, Donkey):
    pass

mul=Mul()
print(mul.speed)
print(mul.strenghy)
mul.print_strenghy()


class Human1:
    def m(self):
        print("I`m Human1")


class Child1(Human1):
    def m(self):
        print("I`m Child1")


class Child2(Human1):
    def m(self):
        print("I`m Child2")

class GrandChild(Child1,Child2):
    def m_from_child_2(self):
        Child2.m(self)


    def m_from_hunan(self):
        Human1.m(self)

    def m(self):
        print("I`m GrandChild")

a = GrandChild()
a.m()
a.m_from_child_2()
a.m_from_hunan()

print(GrandChild.mro())


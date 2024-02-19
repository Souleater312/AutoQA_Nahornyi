
class Human:
    def __init__(self,name:str, age:int, salary, job_position, hair_color):
        self.name = name
        self.age = age
        self.salary = salary
        self.job_position = job_position
        self.hair_color = hair_color


    def get_name(self):
        return self.name

    @classmethod
    def from_name_and_age(cls, name, age):
        return cls(name, age, None, None, None)


    @staticmethod
    def count_bonus(salary):
        return salary * 1.2

class Dog:
    owner_friends = []


"""john = Human()
evelynn = Human()
print(john.name)
print(evelynn.name)
john.name = "john1"
evelynn.name = "evelynn"
print(john.name)
print(evelynn.name)
john.friends.append("Mike")
evelynn.friends.append("Julia")
print(john.friends)
print(evelynn.friends)
good_boy = Dog()
good_boy.owner_friends += evelynn.friends
print(f"Good boy owner friends: {good_boy.owner_friends}")"""
john = Human.from_name_and_age("John", 30)
evelynn = Human.from_name_and_age("Evelynn", 32)
evelynn.salary = 4000
print(john.name)
print(john.get_name())
print(evelynn.get_name())
print(evelynn.count_bonus(evelynn.salary))
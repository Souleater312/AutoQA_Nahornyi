from abc import ABC, abstractmethod

class Cat:
    def make_noise(self):
        pass

class Lion(Cat):
    def __init__(self):
        self.color = "Yellow"
        self.tail = "Long"

    def make_noise(self):
        print("Grrrrrrrr")


class Tiger(Cat):
    def __init__(self):
        self.color = "Three colors"
        self.tail = "Long"

    def make_noise(self):
        print("I`m from 3th OSHB")



class Puma(Cat):
    def __init__(self):
        self.color = "Black"
        self.tail = "Short"

    def make_noise(self):
        print("Buy new shoes")

line = Lion()
line.make_noise()
tiger = Tiger()
tiger.make_noise()
puma = Puma()
puma.make_noise()

class Road(ABC):

    def __init__(self, type_of_cover):
        self.type_of_cover = type_of_cover
        self.__read_width = 4.4

    @abstractmethod
    def bild_range(self):
        pass

    def count_lines(self):
        return self.__read_width / 2.2

    @property
    def road_width(self):
        return self.__read_width

    @road_width.setter
    def road_width(self, r_width):
        self.__read_width = r_width

class Sand(Road):

    def __init__(self):
        super().__init__("Sand")

    def bild_range(self, km):
        print(f"We have bilded {km} km of {self.type_of_cover}")

class Asphalt(Road):

    def __init__(self):
        super().__init__("Asphalt")


    def __make_bitum(self):
        print("boil the bitum")

    def bild_range(self, km):
        self.__make_bitum()
        print(f"We have bilded {km} km of {self.type_of_cover}")


sand = Sand()
sand.bild_range(12)

asphalt = Asphalt()
asphalt.bild_range(11)
asphalt.road_width
print(asphalt.road_width)
asphalt.road_width =2
print(asphalt.road_width)

from abc import ABC, abstractmethod
class OrderPart:

    def dish(self):
        return [Borscht(), Varenyky(), VarenykyPotatoes(), Varenykycherry(), Holubtsi(), Kartoplianky(), Syrniki()]

    def show_menu(self):
        for dish in menu:
            print(dish)

    def make_order(self):
        pass

    def add_in_order(self):
        pass

    def cancel_order(self):
        pass

class Dish(ABC):
    @abstractmethod
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} - {self.price}"

class Borscht(Dish):
    def __init__(self, name="borscht", price=30):
        super().__init__(name, price)

class Varenyky(Dish):
    def __init__(self, name="varenyky", price="choose a filling for varenyky"):
        super().__init__(name, price)

class VarenykyPotatoes(Dish):
    def __init__(self, name="varenyky with potatoes", price=50):
        super().__init__(name, price)

class Varenykycherry(Dish):
    def __init__(self, name="varenyky with cherry", price=55):
        super().__init__(name, price)

class Holubtsi(Dish):
    def __init__(self, name="holubtsi", price=40):
        super().__init__(name, price)

class Kartoplianky(Dish):
    def __init__(self, name="kartoplianky", price=25):
        super().__init__(name, price)

class Syrniki(Dish):
    def __init__(self, name="syrniki", price=45):
        super().__init__(name, price)

dish1 = Kartoplianky()
dish2 = Syrniki()

print(dish1,"\n", dish2)
print(OrderPart.show_menu)
for dish in menu:
    print(dish)
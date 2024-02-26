from lesson_17.factories.abc_beer_factory import BeerFactory
from lesson_17.factories.sorts_of_bear.milk import Milk
from lesson_17.factories.sorts_of_bear.dry import Dry

class StoutFactory(BeerFactory):
    _beer_type = "stout"

    def __init__(self):
        self.name = "Heinikenn"
        self._positions = ["milk", "dry"]

    @property
    def positions(self):
        return self._positions

    def brew_beer(self, name):
        if name == "milk":
            return Milk()
        elif name == "dry":
            return Dry()
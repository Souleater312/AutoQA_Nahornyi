from lesson_17.factories.staut_factory import StoutFactory
from lesson_17.factories.lager_factory import LagerFactory


class AbstractBeerFactory:

    @staticmethod
    def get_factory(beet_type):
        if beet_type == "lager":
            return LagerFactory()
        elif beet_type == "stout":
            return StoutFactory()


lager_factory = AbstractBeerFactory.get_factory("lager")
bottle_of_ale = lager_factory.brew_beer("ale")
print(bottle_of_ale)

import copy

class Building:
    def __init__(self, name, address):
        self.__name = name
        self.__address = address
        self.__stage = dict()

    def __len__(self):
        return len(self.__stage)

    def __setitem__(self, key, value):
        self.__stage[key] = value

    def __getitem__(self, item:int):
        return self.__stage[item]

    def __copy__(self):
        return copy.copy(self)

    # def __deepcopy__(self, memodict={}):
class Company:
    def __init__(self, name, industry):
        self.__name = name
        self.__industru = industry

    @property
    def name(self):
        return self.__name

    @property
    def industry(self):
        return self.__industru



if __name__ == "__main__":
    building1 = Building("Twice Tower", "Myloslacska 65")
    print(len(building1))
    openai = Company("OpenIA", "artificial intelligence")
    nails_company = Company("Best Nails", "beauty")
    building1[1] = openai
    building1[2] = nails_company
    print(len(building1))
    print(building1[2].name)
    building2 = copy.deepcopy(building1)
    print(building1[2].name == building2[2].name)
    print(building1[2] is building2[2])
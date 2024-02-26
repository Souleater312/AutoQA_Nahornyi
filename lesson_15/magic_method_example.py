import datetime

class Rat:
    attemps_to_reach_parametr
    def __init__(self):
        self.__color = "Brown"

   # def __str__(self):
    #    return f"I`m smol rat with {self.__color} fur"

   # def __repr__(self):
    #    return "Rat()"

    def __getattr__(self, item):
        if item == "cool":
            self.attemps_to_reach_parametr.append(datetime.datetime.now)
            return "your attemps to reach parametr was notified"
        else
            return f"Sorry  but {item} is not supported for now"


smol_rat = Rat()
#print(smol_rat)
#smol_rat_2 = eval(repr(smol_rat))
print(smol_rat.cool)
print(smol_rat.cool)
for attempt in smol_rat.atte
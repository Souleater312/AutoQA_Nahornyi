"""
def name_greeter():
    your_name = input("hi please tell me what`s your name")
    print(f"hallo {your_name}")

name_greeter()

def im_a_new_cool_func(value, value2):
    print(value**value2)

im_a_new_cool_func(6,3)

def print_full_name(first_name,last_name, birthdate=0):
    print(f"Full name is {first_name} {last_name}, amd I was born on {birthdate}")

print_full_name("Mykhailo", "Nagornyi", 26111996)
print_full_name(first_name="Mykhailo", last_name="Nahornyi")

def my_favorite_languege(name, languege= 'Python'):
    print(f"Hi, my name is {name}, and my favourite languege is {languege}")

my_favorite_languege("Alex", "Java")
my_favorite_languege("Mykyta")


def mr_sun_two_number(firsr_number, second_number)->int:
    return firsr_number+second_number
new_value = mr_sun_two_number(1234112412,1211212433)
print(new_value)

def make_pizza(*ingtidiens):
    for ingr in ingtidiens:
        print(f'{ingr} is a {ingtidiens.index(ingr)} number in pizza cooking')

make_pizza("cheeese")
make_pizza("cheeese", "cheeese2", "cheeese3", "cheeese4")
make_pizza("pineapple", "curse")
"""
def dogs(**dog_info):
    for key, value in dog_info.items():
        print(f"{key} : {value}")


def sum_and_diff(first_number, second_number):
    return first_number+second_number, first_number-second_number


if __name__ == "__main__":
    dogs(first_name="patrin", required_amount=1000000, cooler_than="iphon")


    #*args
    #**kwargs

    dog_dict = {"1":1, "2":2}
    dog_items = dog_dict.items()


    sum_resulr,diff_result = sum_and_diff(5,10)
    print(sum_resulr)
    print(diff_result)

    sum_and_diff_result = sum_and_diff(20,10)
    print(sum_and_diff_result)
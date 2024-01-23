import math

def func_mane():
    pass


# lambda arg1, arg2.......agrn: expression

double = lambda x: x * 2
print(double(2))
print(double(3))
print(double(4))
print(double(5))


def func_double(x):
    return x * 2


def to_cube(x):
    return x ** 3


lambda_to_cube = lambda x: x ** 3

print(to_cube(3))
print(lambda_to_cube(3))
print(to_cube(4))
print(lambda_to_cube(4))

lambda_multiple_tree = lambda a, b, c: a * b * c
print(lambda_multiple_tree(2, 3, 4))

sqrt_x = lambda x: math.sqrt(x)
print(sqrt_x(4))

lambda_list = [
    lambda x: x*2,
    lambda x: x*3,
    lambda x: x*4,
    lambda x: x*5
]
print(lambda_list[0](2))
for element in lambda_list:
    print(element(6))

lambda_tuple = (
    lambda x: x*x,
    lambda x: x*x*x,
    lambda x: x*x*x*x
)
for element in lambda_tuple:
    print(element(10))

areas_dictionary = {
    "circle" : lambda r: math.pi*r*r,
    "recranhle": lambda a, b: a*b,
    "square": lambda a: a*a
}
print(areas_dictionary["square"](4))
print(areas_dictionary["recranhle"](2,4))
print(areas_dictionary["circle"](6))

list_a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
filtered_list = list(filter(lambda x: x % 2 == 0, list_a))
filtered_odd_list = list(filter(lambda x: x % 2 != 0, list_a))
print(filtered_list)
print(filtered_odd_list)

duble_list = list(map(lambda x: x*2, list_a))
print(duble_list)

double_list_but_in_differ_way = list(map(func_double, list_a))
double_lists = list(map(lambda a, b: a+b, list_a, list_a))
triple_lists = list(map(lambda a, b, c: a+b+c, list_a, list_a, list_a))
print(double_lists)
print(triple_lists)
print(double_list_but_in_differ_way)
list_of_letters = ["a", "s", "d", "f", "g", 2]
from functools import reduce
sum_body = reduce(lambda x, y: x + y, duble_list)
sum_body_2 = reduce(lambda x, y: x + y if type(y) == str else x+str(y), list_of_letters)
print(sum_body)
print(sum_body_2)

list_b = [90, 50, 40, 20, 30, 60]
min_el = reduce(lambda a,b: a if (a<b) else b, list_b)
min_el_but_diff = reduce(min, list_b)
print(min_el)
print(min_el_but_diff)
max_number = lambda x, y: x if x>y else y
print(max_number(12,33))

list_c = [[15,9,12], [1,4,7], [20,10]]
sorted_list = lambda x: (sorted(el) for el in x)
print(list_c)
print(list(sorted_list(list_c)))

list_c = [[15, 9, 12], [1, 4, 7], [20, 10]]
sorted_list = sorted(list_c, key=lambda x: min(x))
print(sorted_list)
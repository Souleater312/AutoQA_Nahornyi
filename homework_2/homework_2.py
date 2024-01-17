import random
import math

# Задача 1
print("Задача 1")
minute = random.randint(0, 59)
print(minute)
if minute <= 15:
    print("It's the first quarter.")
elif 15 < minute <= 30:
    print("It's the second quarter.")
elif 30 < minute <= 45:
    print("It's the third quarter.")
else:
    print("It's the fourth quarter.")
# Задача 2
print("Задача 2")
birth_month = input("Введіть номер місяця вашого народження:")
if birth_month in ["12", "1", "2"]:
    print("За вікном падав сніг")
elif birth_month in ["3", "4", "5"]:
    print("Все довкола розцвітало")
elif birth_month in ["6", "7", "8"]:
    print("Діти насолоджувались літніми канікулами")
elif birth_month in ["9", "10", "11"]:
    print("Все довкола загоралось яскравими фарбами")
else:
    print("Помилка: Неправильний номер місяця")
# Задача 3
print("Задача 3")
random_number = random.randint(0, 1000000)
number_str = str(random_number)
last_digit = int(number_str[-1])
sum_digits = sum(int(digit) for digit in number_str)
dilenna_na_2 = str(last_digit/2)
remainder_divided_by_2 = dilenna_na_2.split(".")
dilenna_na_3 = str(sum_digits/3)
remainder_divided_by_3 = dilenna_na_3.split(".")
if (remainder_divided_by_2[1] == "0" and remainder_divided_by_3[1] == "0"):
    ###(last_digit % 2 == 0 and sum_digits % 3 == 0): можна використати спрощений варіант
    print(f"The number {random_number} is divisible by 6")
else:
    print(f"The number {random_number} is not divisible by 6")

# Задача 4
print("Задача 4")
input_x = input("Enter the value on the X-axis:")
input_y = input("Enter the value on the Y-axis:")
try:
    x = float(input_x)
    y = float(input_y)
    if x > 0 and y > 0:
        print(f"The point ({x}, {y}) belongs to the first quadrant.")
    elif x < 0 and y > 0:
        print(f"The point ({x}, {y}) belongs to the second quadrant.")
    elif x < 0 and y < 0:
        print(f"The point ({x}, {y}) belongs to the third quadrant.")
    elif x > 0 and y < 0:
        print(f"The point ({x}, {y}) belongs to the fourth quadrant.")
    elif x == 0 and (y < 0 or y > 0):
        print(f"The point ({x}, {y}) lies on the X-axis.")
    elif y == 0 and (x < 0 or x > 0):
        print(f"The point ({x}, {y}) lies on the Y-axis.")
    else:
        print(f"The point ({x}, {y})  is the origin (origin of coordinates).")
except ValueError:
   print("Incorrect coordinates are specified")

import random

# Завдання 1
print("Завдання 1")


def select_same_number(list_1, list_2):
    selected_list = []
    for element in list_1:
        if element in list_2:
            selected_list.append(element)
    if selected_list:
        print("Common numbers in ascending order:", sorted(selected_list))
    else:
        print("There are no common numbers in the lists.")


select_same_number([1, 2, 5, 4], [2, 5, 4])
lisr1 = [1, 3, -4, 4, 5]
list2 = [-1, -4, 5, 1, 4]
select_same_number(list2, lisr1)

# Завдання 2
print("Завдання 2")


def students_surpass_average(**student_info):
    sum_value = sum(student_info.values())
    average = sum_value / len(student_info)
    for key, value in student_info.items():
        if value >= average:
            print(f" {key} : {value}")


students_surpass_average(Vitaliy=65, Anna=70, Oleg=100, Kateryna=93, Vadym=80, Hlib=70)

# Завдання 3
print("Завдання 3")


def randome_value(my_list):
    if not my_list:
        return None
    else:
        return random.choice(my_list)


def my_dictionary(**kwarcgs):
    return_dict = kwarcgs
    return return_dict


name = ["Kateryna", "Petro", "Olena", "Ihor", "Yulia", "Oleksandr"]
surname = ["Romanenko", "Tkachenko", "Morozov", "Hrytsenko", "Kovalchuk", "Ivanenko"]
location = ["Kyiv", "Lviv", "Odesa", "Kharkiv", "Dnipro", "Lutsk"]

print(my_dictionary(name=randome_value(name), surname=randome_value(surname), location=randome_value(location)))

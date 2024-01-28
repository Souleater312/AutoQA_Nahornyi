# Завдання 1
print("Завдання 1")
list_a = [1,3,2,4,5,"d"]
list_b = [1,4,6,7,"d"]
lambda_is_same = list(filter(lambda x: x in list_a, list_b))
print(lambda_is_same)
# Завдання 2
print("Завдання 2")
list_a2 = [1, 2, 3, 4, "3"]
list_b2 = [3, 2, 1, 5, 7, 8]
lambda_is_digital = lambda a:  all(isinstance(x, (int, float)) for x in a)
print(lambda_is_digital(list_a2))
print(lambda_is_digital(list_b2))
# Завдання 3
print("Завдання 3")
list_a3 = list(input("Enter first list:"))
list_b3 = list(input("Enter second list:"))
lambda_check_len = lambda a,b: f"First list {a} larger than the list {b}" if (len(a) > len(b)) else f"Second list {b} larger than the list {a}" if len(b) > len(a) else "Two lists are of equal length"
print(lambda_check_len(list_a3,list_b3))

#Задача 4 (задача з уроку, про фільтрацію кожного масива та загального масива за сумою елементів)
print("Завдання 4")
list_extra = [[15,9,12], [6,4,7], [20,10]]
print(list_extra)
sorted_list = lambda x: [sorted(el) for el in x]
sort_matrix = lambda x: [sorted(el) for el in sorted(x, key=lambda x: sum(sorted(x)))]
print(sorted_list(list_extra))
print(sort_matrix(list_extra))


#Задача 5 (задача з уроку, оюєднати в один масив та відфільтрувати за значенням)
#print("Завдання 5")
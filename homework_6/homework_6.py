import re

# Завдання 1
print("Завдання 1")
pattern = re.compile("\W")
your_str = input("Input your str:")
if pattern.search(your_str) == None:
    print(f"'{your_str}' contains only [a-zA-Z0-9_]")
else:
    print(f"'{your_str}' contains not only [a-zA-Z0-9_]")

# Завдання 2
print("Завдання 2")

input_str = ["example (.com)", "github (.com)", "stackoverflow (.com)"]

for i in input_str:
    result = re.sub("\s*\([^)]*\)", "", i)
    print(result)

# Завдання 3
print("Завдання 3")

input_str = "TextInUppercaseWithoutSpaces"
result = re.sub("(?=[A-Z])", " ", input_str)
print(result)
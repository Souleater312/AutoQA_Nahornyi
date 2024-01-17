'''first_list = [1,3,6,3,9,4,7,11,5]
print(first_list)
a = [1,2,3,4]
b = a
a.append(5)
b.append(6)
print(a)
print(b)
c = a.copy()
c.pop()
print(a)
print(c)

z = [1,2]
x = [3,4]
v = z + x
z.pop()
print(z)
print(v)
d = list(z)
'''
first_list = [1,5,3,5,7,3,4,5,7]
print(first_list.count(5))
first_list.reverse()
print(first_list)
first_tuple = (4,5,6,7,8)
print(first_tuple[0])
elements_list=[]
for element in first_list:
    if element>5:
        elements_list.append(element)
print(elements_list)
counter = 0
while counter<10:
    print("help me")
    counter+=1
for i in "hello world":
    if i == "o":
        continue
    print(i)
while counter<20:
    counter+=1
    if counter%2 == 1:
        continue
    print(counter)
while counter<20:
    counter+=1
    if counter%2 == 1:
        break
    print(counter)

for i in "hello_world":
    if i == "o":
        print(f"this string have {i} letters")
        break
else:
    print("dont have a letters")

a = 0
print()
while True:
    new_a = input("Enter a number or sum:")
    if new_a == "sum":
        print(a)
        break
    elif new_a.startswith("-") and new_a[1:] or new_a.isnumeric():
        a += int(new_a)
    else:
        print("Not a number")

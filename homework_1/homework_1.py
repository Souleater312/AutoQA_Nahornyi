import math
# Завдання 1
print("Завдання 1")
name = "Mykhailo"
surename = "Nahornyi"
full_name = name+" "+surename
print(full_name)
print(full_name.lower())
print(full_name.upper())
name = "mykhailo"
surename = "nahornyi"
print(full_name.title())
name = "     \tMykhailo"
surename = "Nahornyi\n     "
full_name = name+" "+surename
print(full_name.strip())
full_name2 = name.lstrip()+" "+surename.rstrip()
print(full_name2)
name = "Mykhailo"
surename = "Nahornyi"
full_name = "\t"+name+"\n"+"\t"+surename
print(full_name)

#Завдання 2
print("Завдання 2")
r = input("Enter circle radius:")
c = 2 * math.pi * float(r)
s = math.pi * float(r)**2
print(f"Circle Radius: {r}")
print(f"Circle Area: {s}")
print(f"Circle сircumference: {c}")
#Завдання 3
print("Завдання 3")
current_rate = 38.5996
convert1000 = 1000/current_rate
rounded_cunvert = round(convert1000, 2)
print(f"Поточний курс складає: {current_rate}")
print(f"1000 гривнів за поточним курсом складає: {rounded_cunvert}$")

from lesson_6.func_examle import sum_and_diff

a,b = sum_and_diff(500,100)
print(a)
print(b)

def check_number(number1,number2=0):
   your_number = int(input("Enter your number: "))
   if number1 < your_number < number2:
       print(f"Uppi: {your_number} in between {number1} and {number2}")
       return True
   else:
       print("Wrong number")
       return False


"""result = check_number(1,20)
print(result)"""

def str_without(*not_this):
    your_str = input("Enter your str:")

    for str1 in your_str:
        if str1 in not_this:
            your_str=your_str.replace(str1, "")
    return your_str

a = str_without("3", "5", "7")
print(a)
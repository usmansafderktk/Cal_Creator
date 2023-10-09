
print("Let's create a working calculator")

number = 0
option = 0
while number != "done":
    number = input("Give input you wish to do calculation on or are you done?")
    try:
        number= int(number)
    except ValueError:
        print("This is not an valid integer.")
    while option != "=":
        option = input("if you want to add, subtract, divide, multiply or do modulus ,\n enter '+', '-' , '/' , '*' , '%' respectively or if you want to calculate write result = \n")
        if option == "=":
            print(number)
            break
        num = int(input("Enter second number to do calulation"))
        if option == "+":
            number += num
            print(number)
        elif option == "-":
            number -= num
            print(number)
        elif option == "*":
            number *= num
            print(number)
        elif option == "/":
            number /= num
            print(number)
        elif option == "%":
            number %= num
            print(number)
        else:
            print("Not a Valid INPUT")


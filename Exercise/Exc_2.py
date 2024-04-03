num = int(input("Your number: "))

if num % 4 == 0:
    print("The number is multiple of 4!")
elif num % 2 == 0:
    print("This is an even number!")
else:
    print("This is an odd number!")

number = int(input("Type in your number: "))
check = int(input("Type in second number to check: "))

if number % check == 0:
    print("Check divides evenly into your number!")
else:
    print("Check does not divides evenly into your number!")
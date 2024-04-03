list = []

user_number = int(input("Your number: "))

for number in range(1, user_number+1):
    if user_number % number == 0:
        list += [number]
print(list)






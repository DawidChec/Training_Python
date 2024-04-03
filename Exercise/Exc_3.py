list = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
new_list = []
newer_list = []

for number in list:
    if number <= 5:
        new_list.append(number)
print(new_list)

user_number = int(input("Your number: "))

for number in list:
    if number <= user_number:
        newer_list.append(number)
print(newer_list)

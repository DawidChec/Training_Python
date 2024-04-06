import random

list_with_duplicates = []
list_without_duplicates = []

def create_list_with_duplicates():
    for i in range(0,10):
        list = random.randint(1, 10)
        list_with_duplicates.append(list)
    return (list_with_duplicates)

def remove_duplicates():
    for number in list_with_duplicates:
        if number not in list_without_duplicates:
            list_without_duplicates.append(number)
    return (list_without_duplicates)


print(create_list_with_duplicates())
print(remove_duplicates())


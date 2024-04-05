import random

random_list = []

for element in range (0, 100):
    a = random.randint(0, 100)
    random_list.append(a)

def get_element(element):
    res = random_list[::len(random_list)-1]
    print(res)

get_element(random_list)

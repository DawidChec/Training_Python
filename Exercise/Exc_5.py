import random

random_list_a = []
random_list_b = []
final_list = []

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = []

for number in a:
    if number in b and number not in c:
        c.append(number)
#print(c)

for a in range(0,10):
    a = random.randint(0,10)
    random_list_a.append(a)
    print(random_list_a)
for b in range(0,10):
    b = random.randint(0,10)
    random_list_b.append(b)
    print(random_list_b)

for number in random_list_a:
    if number in random_list_b and number not in final_list:
        final_list.append(number)
print(final_list)




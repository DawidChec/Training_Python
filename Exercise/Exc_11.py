
def check_if_prime(num):
    for i in range(2, num):
        if num % i == 0:
            print("Your number is: Not Prime")
            break
    else:
        print("Your number is: Prime")
def get_integer():
    return int(input("Type in your number and we will check if it is a prime number: "))

check_if_prime(get_integer())
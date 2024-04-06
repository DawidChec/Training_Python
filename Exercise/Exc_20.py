a = [1, 4, 5, 7, 9, 12, 56, 87, 45, 87, 92, 99]

def check_if_number(i):
    for number in a:
        if i == number:
            print("Your number is in the list!")
            break
        elif i != number:
            print("Your number is not in the list!")
            break
def play_again(a):
    if a != "y":
        exit()

if __name__ == '__main__':

    while True:
        user_input = int(input("Type in your number to check: "))

        check_if_number(user_input)

        user_choose = input("Type in 'y' to continue game, if not press anything else: ")

        play_again(user_choose)









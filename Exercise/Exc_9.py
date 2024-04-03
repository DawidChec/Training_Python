import random

while True:
    a = random.randint(1,9)
    print(a)

    user_guess = int(input("Welcome in game! Guess the generated number: "))

    if user_guess == a:
        print('Congrats! You guessed!')
    elif user_guess == a -1:
        print('Your guess was minus one number to low!')
    elif user_guess == a +1:
        print('Your guess was plus one number to high!')
    else:
        print('Not even close!')

    exit_game = input('Type in "Exit" if you wish to exit the game or any other button to continue.')
    if exit_game == "Exit":
        break

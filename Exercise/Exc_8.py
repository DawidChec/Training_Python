
while True:
    print("Welcome! This is Rock, Paper, Scissors game!")

    name_player_one = input("Type in name of player one: ")
    name_player_two = input("Type in name of player two: ")

    print("Type in 'r' for rock, 'p' for paper, and 's' for scissors.")

    player_one_weapon = input(f"{name_player_one} choose your weapon!: ")
    player_two_weapon = input(f"{name_player_two} choose your weapon!: ")

    if player_one_weapon == "r" and player_two_weapon == "s":
        print(f"Rock beats scissors, {name_player_one} wins! ")
    if player_one_weapon == "p" and player_two_weapon == "s":
        print(f"Paper loses to scissors, {name_player_two} wins!")
    if player_one_weapon == "s" and player_two_weapon == "p":
        print(f"Scissors wins against paper, {name_player_one} wins!")

    if player_one_weapon == "r" and player_two_weapon == "p":
        print(f"Rock loses to paper, {name_player_two} wins! ")
    if player_one_weapon == "p" and player_two_weapon == "r":
        print(f"Paper wins against rock, {name_player_one} wins!")
    if player_one_weapon == "s" and player_two_weapon == "r":
        print(f"Scissors loses against rock, {name_player_two} wins!")
    if player_one_weapon == "r" and player_two_weapon == "r":
        print("It's a tie!")
    if player_one_weapon == "p" and player_two_weapon == "p":
        print("It's a tie!")
    if player_one_weapon == "s" and player_two_weapon == "s":
        print("It's a tie!")

    play_again = input("Do you wish to play again?(Y/N)")
    if play_again == "N":
        break




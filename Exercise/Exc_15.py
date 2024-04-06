
def revers_a_string():
    user_string = input("Enter a long string containing multiple words. ")
    result = user_string.split(" ")
    revesed_string = result[::-1]
    return revesed_string

print(revers_a_string())



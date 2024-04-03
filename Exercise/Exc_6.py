def is_palindrome(text):
    lenght = len(text)

    for i in range(0, lenght // 2):
        if (text[i] != text [lenght -i - 1]):
            return False

    return True

string_one = "racecar"
print(is_palindrome(string_one))

string_two = "Bkukker"
print(is_palindrome(string_two))


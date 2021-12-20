def main():
    word = read_word()
    decision = check_palindrome(word)
    print('The word "' + word + '" ' + decision)
    input('Press "Enter" to continue ...')


def read_word():  # Asks a user to write a word and reads it
    word = input('Write a word and press Enter:' + '\n')
    return word


def check_palindrome(word):  # Checks if a word is a palindrome
    low_word = word.lower()  # The word may be written incorrectly, let's make it in lower case
    if low_word == low_word[::-1]:
        decision = 'is a palindrome'
    else:
        decision = 'is not a palindrome'
    return decision


if __name__ == "__main__":
    main()

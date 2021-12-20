def main():
    string = read_string()
    num_diff_sym = diff_symbols(string)
    print('The number of different symbols in the string is ' + str(num_diff_sym) + ' symbols.')
    input('Press "Enter" to continue ...')


def read_string():  # Asks a user to write a string and reads it
    string = input('Write a string and press Enter:' + '\n')
    return string


def diff_symbols(string):  # Counts a number of different symbols in a string
    chars = set(string)
    # Sorts a string ex. ("mom washed a window" >> {'M', 's', 'i', 'w', 'n', 'h', 'm', 'e', 'd', 'o', ' ', 'a'})
    num_diff_sym = len(chars)
    return num_diff_sym


if __name__ == "__main__":
    main()

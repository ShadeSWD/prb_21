def main():
    string = read_string()
    len_string = count_string(string)
    print('The length of the string is ' + str(len_string) + ' symbols.')
    input('Press "Enter" to continue ...')


def read_string():  # Asks a user to write a string and reads it
    string = input('Write a string and press Enter:' + '\n')
    return string


def count_string(string):  # Counts a numbers of symbols in a "string"
    len_string = len(string)
    return len_string


if __name__ == "__main__":
    main()

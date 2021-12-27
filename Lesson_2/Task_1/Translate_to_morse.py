def input_phrase():
    phrase = input('Enter the phrase. It must contain only English and Russian letters and "space": \n')
    return phrase


def to_morse(phrase):  # to save time the dictionary is made only for English letters
    upp_phrase = phrase.upper()

    morse_key = {"A": "*_ ", "B": "_*** ", "C": "_*_* ", "D": "_** ", "E": "* ", "F": "**_* ", "G": "__* ",
                 "H": "**** ", "I": "** ", "J": "*___ ", "K": "_*_ ", "L": "*_** ", "M": "__ ", "N": "_* ", "O": "___ ",
                 "P": "*__* ", "Q": "__*_ ", "R": "*_* ", "S": "*** ", "T": "_ ", "U": "**_ ", "V": "***_ ",
                 "W": "*__ ", "X": "_**_ ", "Y": "_*__ ", "Z": "__** ", " ": " "}

    morse_phrase = ''

    for i in range(0, len(upp_phrase)):

        morse_phrase += morse_key[upp_phrase[i]]

    return morse_phrase


def main():
    phrase = input_phrase()
    morse_phrase = to_morse(phrase)
    print(morse_phrase)


if __name__ == "__main__":
    main()

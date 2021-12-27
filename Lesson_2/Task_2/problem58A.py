# https://codeforces.com/problemset/problem/58/A


def data_input():
    word = input()
    return word


def hello_check(word):
    key = "hello"
    if len(word) < len(key):
        print('NO')
    else:
        i5 = word.rfind('o') + 1  # str.rfind(sub[, start[, end]]) -> int
        i4 = word.rfind('l', 0, i5 - 1) + 1
        i3 = word.rfind('l', 0, i4 - 1) + 1
        i2 = word.rfind('e', 0, i3 - 1) + 1
        i1 = word.rfind('h', 0, i2 - 1) + 1
        i = i1 * i2 * i3 * i4 * i5
        print('NO' if i == 0 else 'YES')


def main():
    word = data_input()
    hello_check(word)


if __name__ == "__main__":
    main()

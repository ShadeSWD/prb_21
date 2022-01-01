# https://codeforces.com/problemset/problem/58/A
i = 0


def data_input():
    word = input()
    return word


def hello_check(word):
    global i
    key = "hello"
    if len(word) < len(key):
        print('NO')
    else:
        i = word.rfind(key[-1]) + 1
        check = i
        for s in range(len(key) - 1):
            k = word.rfind(key[- 2 - s], 0, i - 1) + 1
            i = k
            check *= k
        print('NO' if check == 0 else 'YES')


def main():
    word = data_input()
    hello_check(word)


if __name__ == "__main__":
    main()

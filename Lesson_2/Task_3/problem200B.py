# https://codeforces.com/problemset/problem/200/B


def main():
    n, concentration = data_input()
    final = concentration_calculator(n, concentration)
    print(final)


def data_input():
    n = int(input())
    concentration = list(map(int, input().split()))
    return n, concentration


def concentration_calculator(n, concentration):
    juice = 0
    for i in range(0, n):
        juice += concentration[i]
    final = juice/n
    return final


if __name__ == "__main__":
    main()

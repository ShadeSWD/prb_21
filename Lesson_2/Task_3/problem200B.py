# https://codeforces.com/problemset/problem/200/B

import statistics


def main():
    n, concentration = data_input()
    final = concentration_calculator(concentration)
    print(final)


def data_input():
    n = int(input())
    concentration = list(map(int, input().split()))
    return n, concentration


def concentration_calculator(concentration):
    final = statistics.mean(concentration)
    return final


if __name__ == "__main__":
    main()

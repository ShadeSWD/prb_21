# https://codeforces.com/problemset/problem/1360/C


def main():
    num = read_num_of_tries()
    decision = []
    i = 0
    while i < num:
        n, numbers = data_input()
        decision.append(solve_problem(n, numbers))
        i += 1
    j = 0
    while j < num:
        print(decision[j])
        j += 1


def solve_problem(n, numbers):
    evens = 0
    odds = 0
    for i in range(len(numbers)):
        if check_number(numbers[i]) == 'even':
            evens += 1
        elif check_number(numbers[i]) == 'odd':
            odds += 1
    if check_number(evens) != check_number(odds):
        result = 'NO'
    else:
        if check_number(evens) == 'even':
            result = 'YES'
        else:
            result = try_pairs(n, numbers)
    return result


def try_pairs(n, numbers):
    i = 0
    result = 'NO'
    while i < n:
        j = 1
        while j < n:
            if check_number(numbers[i]) != check_number(numbers[j]) and abs(numbers[i] - numbers[j]) == 1:
                result = 'YES'
            j += 1
        i += 1
    return result


def check_number(number):
    if number % 2 == 0:
        result = 'even'
    else:
        result = 'odd'
    return result


def data_input():
    n = int(input())
    numbers = list(map(int, input().split()))
    return n, numbers


def read_num_of_tries():
    num = int(input())
    return num


if __name__ == "__main__":
    main()

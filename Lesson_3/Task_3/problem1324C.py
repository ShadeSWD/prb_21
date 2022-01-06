# https://codeforces.com/problemset/problem/1324/C


def main():
    num = read_num_of_tries()
    d = []
    for i in range(num):
        directions = data_input()
        d.append(solve_problem(directions))
    for i in range(num):
        print(d[i])


def solve_problem(directions):
    d = 0
    for i in range(len(directions)):
        k = 1
        while i < len(directions):
            if directions[i] == 'L':
                k += 1
                i += 1
            else:
                break
        if d < k:
            d = k
    return d


def data_input():
    directions = list(map(str, input()))
    directions.append('R')  # place, the frog wants to get
    return directions


def read_num_of_tries():
    num = int(input())
    return num


if __name__ == "__main__":
    main()

def data_input():  # collects the information about the situation

    n, t = map(int, input().split())  # n - number of kids, t - the current time we want to know the situation

    row = list(map(str, input()))  # a row is a sequence of boys and girls at time = 0

    return n, t, row


def que_status(n, t, row):  # gives the status of the que at the time = t
    time = 1  # time of the calculation
    while time <= t:
        pos = 0  # position of the calculation
        while pos < n - 1:
            if row[pos] == 'B' and row[pos + 1] == 'G':  # if true the boy lets the girl forward
                row[pos] = 'G'
                row[pos + 1] = 'B'
                pos += 2
            else:  # nothing to do, just change the position
                pos += 1
        time += 1
    m_row = row
    return m_row


def main():
    n, t, row = data_input()
    m_row = que_status(n, t, row)
    print("".join(m_row))


if __name__ == '__main__':
    main()

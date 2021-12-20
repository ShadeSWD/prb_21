def data_input():  # collects the information about the world and its teleports

    n, t = map(int, input().split())  # n - number of cells, t - the cell I want to go to

    telecode = list(map(int, input().split()))  # a telecode is (n - 1) of integer numbers for the teleport

    return n, t, telecode


def check_teleport(end_pos, telecode):  # checks if the voyage is available

    start_pos = 0  # my start position is in the cell 0 + 1 = 1
    curr_pos = start_pos  # I am NOW in start position

    while curr_pos < end_pos - 1:  # I move through the world while I am lower than I want to be
        curr_pos = curr_pos + telecode[curr_pos]

    if curr_pos == end_pos - 1:  # get the decision
        decision = 'YES'
    else:
        decision = 'NO'

    return decision


def main():

    n, t, telecode = data_input()
    decision = check_teleport(t, telecode)
    print(decision)

    input('Press "Enter" to continue ...')


if __name__ == '__main__':
    main()

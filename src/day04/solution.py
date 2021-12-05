from collections import deque

def is_complete(board, drawn):
    return any(set(i) <= drawn for i in board) or any(set(i) <= drawn for i in zip(*board))

def win(boards, draws, drawn = None):
    draws, drawn, complete = draws.copy(), drawn or [], []
    while not complete:
        drawn += [draws.popleft()]
        complete = [i for i in boards if is_complete(i, set(drawn))]
    return complete[0], drawn

def lose(boards, draws):
    draws, drawn = draws.copy(), []
    while len(boards) > 1:
        drawn += [draws.popleft()]
        boards = [i for i in boards if not is_complete(i, set(drawn))]
    return boards, draws, drawn

def score(board, drawn):
    undrawn = set(j for i in board for j in i) - set(drawn)
    return sum(int(i) for i in undrawn) * int(drawn[-1])

if __name__ == "__main__":
    with open("src/day04/input.txt") as f:
        draws, *boards = [i.split('\n') for i in f.read().strip().split('\n\n')]
        draws = deque(draws[0].split(','))
        boards = [[j.split() for j in i] for i in boards]

        print("Part1:", score(*win(boards, draws)))
        print("Part2", score(*win(*lose(boards, draws))))

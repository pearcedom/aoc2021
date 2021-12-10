from statistics import median

def sort_chunks(chunks):
    start2close = dict(zip('{([<', '})]>'))
    starts, closes = set('{([<'), set('})]>')
    corruptions, incompletes = [], []
    for x in chunks:
        start = []
        for i in x:
            if i in starts:
                start.append(i)
                continue
            elif i in closes and i != start2close[start.pop()]:
                corruptions.append(i)
                break
        else:
            incompletes.append(start)
    return corruptions, incompletes

def complete(x):
    start2close = dict(zip('{([<', '})]>'))
    return "".join([start2close[i] for i in reversed(x)])

def score_corruptions(x):
    corruption_scores = {')': 3, ']': 57, '}': 1197, '>': 25137}
    return sum(corruption_scores[i] for i in x)

def score_completions(x):
    return median(score_completion(i) for i in x)

def score_completion(x):
    completion_scores = {')': 1, ']': 2, '}': 3, '>': 4}
    score = 0
    for i in x:
        score *= 5
        score += completion_scores[i]
    return score

if __name__ == '__main__':
    with open('src/day10/input.txt') as f:
        chunks = f.read().splitlines()

    corruptions, incompletes = sort_chunks(chunks)
    print("Part1:", score_corruptions(corruptions))
    print("Part2:", score_completions(complete(i) for i in incompletes))

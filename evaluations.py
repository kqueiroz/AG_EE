WORD_BASE = "computacaoevolutiva"
SIZE = 1000
POPULATION = 50

def colisionDiagonal(oneQueen, twoQueen):
    if (abs(oneQueen[0] - twoQueen[0]) == abs(oneQueen[1] - twoQueen[1])):
        return True
    return False


def colisionColumn(oneQueen, twoQueen):
    if (oneQueen[1] == twoQueen[1]):
        return True
    return False


def evaluateEightQueens(individual):
    conflicts = 0
    for i in range(len(individual)):
        solutionOne = [i, individual[i]]
        for k in range(len(individual)):
            solutionTwo = [k, individual[k]]
            if (i == k):
                continue
            if (colisionColumn(solutionOne, solutionTwo) or colisionDiagonal(solutionOne, solutionTwo)):
                conflicts = conflicts + 1
    return conflicts,


def evaluateSecretWord(individual):
    hits = 0
    for i, letter in enumerate(individual):
        if letter == WORD_BASE[i]:
            hits += 1
    rate = hits / len(WORD_BASE)
    return rate,

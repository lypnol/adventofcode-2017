from submission import Submission


class LizzarocSubmission(Submission):
    def run(self, s):
        spiral = dict()
        spiral[(0, 0)] = 1
        value = 1
        i = 0
        j = 0
        directionIdx = 0
        shouldTurnBool = False
        while value < int(s):
            i,j = advance(directionIdx,i,j)
            value = sum(getNeighbours(spiral, i, j))
            spiral[(i,j)] = value
            shouldTurnBool = shouldTurn(i,j)
            if (shouldTurnBool):
                directionIdx = (directionIdx + 1) % 4

        return value

def advance(directionIdx,i,j):
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    # Simply does a tuple addition of (i,j) and directions elem
    return tuple(map(lambda x, y: x + y, (i,j), directions[directionIdx]))

def shouldTurn(i, j):
    return i == j or (i == - j + 1 if i > 0 else i == - j)


def getNeighbours(spiral, i, j):
    neighbours = [[x, y] for x in range(i - 1, i + 2) for y in range(j - 1, j + 2)]
    return map(lambda params: spiral[(params[0], params[1])] if (params[0], params[1]) in spiral else 0, neighbours)

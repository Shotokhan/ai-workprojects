class SearchTree:
    def __init__(self, boardObj):
        self.root = Node(boardObj, -1)
        self.knight = Knight()
        self.current = self.root
        self.visited = set()
        self.visited.add(str(boardObj))

    def A_star(self):
        fringe = [self.root]
        while len(fringe) > 0:
            self.current = fringe.pop(0)
            if self.current.board.heuristic() == 0:
                return self.current.costToPath
            self.current.expand(self.knight)
            for child in self.current.children:
                if str(child.board) not in self.visited:
                    fringe.append(child)
                    self.visited.add(str(child.board))
            fringe = sorted(fringe)
        return -1  # failure

    def getSolutionPath(self):
        path = []
        runner = self.current
        while runner is not None:
            path.append(str(runner.board))
            runner = runner.parent
        return path[::-1]

    def __str__(self):
        lifo = [self.root]
        s = ""
        while len(lifo) > 0:
            current = lifo.pop()
            s += (2 * current.costToPath) * " " + str([str(current.board), f"f(n)={current.cost()}"]) + '\n'
            for child in current.children:
                lifo.append(child)
        return s


class Node:
    def __init__(self, boardObj, costSoFar, parent=None):
        self.board = boardObj
        self.children = []
        self.parent = parent
        self.costToPath = costSoFar + 1

    def cost(self):
        return self.costToPath + self.board.heuristic()

    def expand(self, knight):
        x, y = self.board.getEmpty()
        available = knight.moves(x, y, [0, 3])
        for booth in available:
            newBoard = Board(self.board.get_board())
            newBoard.swap(x, y, booth[0], booth[1])
            child = Node(newBoard, self.costToPath, self)
            self.children.append(child)

    def __lt__(self, other):
        return self.cost() < other.cost()

    def __eq__(self, other):
        return str(self.board) == str(other.board)


class Board:
    def __init__(self, board):
        self.board = board
        self.target = "12345678."

    def get_board(self):
        return self.board.copy()

    def get(self, x, y):
        return self.board[x][y]

    def set_val(self, x, y, val):
        self.board[x] = self.board[x].replace(self.board[x][y], val)

    def getEmpty(self):
        for i in range(3):
            if "." in self.board[i]:
                x = i
                y = self.board[i].index(".")
                return [x, y]
        return -1

    def swap(self, x0, y0, x1, y1):
        tmp = self.get(x0, y0)
        self.set_val(x0, y0, self.get(x1, y1))
        self.set_val(x1, y1, tmp)

    def heuristic(self):
        count = 0
        s = str(self)
        for i in range(len(s)):
            if s[i] == self.target[i]:
                count += 1
        return 9 - count

    def __str__(self):
        s = "".join(self.board)
        return s


class Knight:
    def __init__(self):
        self.tabula = [[-1, -2], [1, -2], [-2, -1], [2, -1], [-2, 1], [2, 1], [-1, 2], [1, 2]]

    def shift(self, x, y):
        shift = []
        for position in self.tabula:
            shift.append([position[0] + x, position[1] + y])
        return shift

    def moves(self, x, y, sqr_boundary):
        available = []
        for position in self.shift(x, y):
            if sqr_boundary[0] <= position[0] < sqr_boundary[1] and sqr_boundary[0] <= position[1] < sqr_boundary[1]:
                available.append(position)
        return available

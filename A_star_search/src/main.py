from src.problem import Board, SearchTree


def run():
    board = ["362", ".58", "147"]
    boardObj = Board(board)
    tree = SearchTree(boardObj)
    print(tree.A_star())
    print()
    # print(tree)
    path = tree.getSolutionPath()
    for state in path:
        print(state[0:3])
        print(state[3:6])
        print(state[6:9])
        print()


if __name__ == "__main__":
    run()

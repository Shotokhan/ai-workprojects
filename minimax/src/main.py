from src.util import skynetParser
from src.minimax import minimax_decision


def run():
    # init_position = 2
    positions = [2, 1, 7, 13, 15]
    skynet = skynetParser('complex_mesh')
    # print(skynet)
    # print(" ".join(str(i) for i in minimax_decision(init_position, skynet)))
    for position in positions:
        print(" ".join(str(i) for i in minimax_decision(position, skynet)))


if __name__ == "__main__":
    run()

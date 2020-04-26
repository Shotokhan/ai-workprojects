from src.util import skynetParser
from src.minimax import minimax_decision


def run():
    # init_position = 2
    positions = [2, 3, 8, 36, 13, 15, 23, 27, 25, 27, 28, 27, 23, 15, 14, 10, 11, 6, 1, 3]
    skynet = skynetParser('complex_mesh')
    skynet.computeDistancesFromGateways()
    # print(skynet)
    # print(" ".join(str(i) for i in minimax_decision(init_position, skynet)))
    for position in positions:
        print(" ".join(str(i) for i in minimax_decision(position, skynet)))


if __name__ == "__main__":
    run()

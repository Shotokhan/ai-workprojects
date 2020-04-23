from src.skynet import Skynet


def skynetParser(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    n, l, e = [int(i) for i in lines[0].split(" ")]
    skynet = Skynet()
    for line in lines[1:l+1]:
        node_1, node_2 = [int(i) for i in line.split(" ")]
        skynet.addLink(node_1, node_2)
    for gateway in lines[l+1:l+1+e]:
        skynet.addGateway(int(gateway))
    return skynet

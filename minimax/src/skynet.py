import copy


class Skynet:
    def __init__(self):
        self.adjacency = {}
        self.gateways = set()

    def __str__(self):
        s = f"Adjacency list: {self.adjacency}" + '\n'
        s += f"Gateways : {self.gateways}"
        return s

    def copy(self):
        simulated = Skynet()
        simulated.adjacency = copy.deepcopy(self.adjacency)
        simulated.gateways = self.gateways  # never gets modified
        return simulated

    def addLink(self, node_1, node_2):
        if self.adjacency.get(node_1) is None:
            self.adjacency[node_1] = []
        self.adjacency[node_1].append(node_2)
        if self.adjacency.get(node_2) is None:
            self.adjacency[node_2] = []
        self.adjacency[node_2].append(node_1)

    def addGateway(self, gateway):
        self.gateways.add(gateway)

    def isGateway(self, node):
        return node in self.gateways

    def cutLink(self, node_1, node_2):
        runtime_constraint = self.adjacency.get(node_1) is not None
        runtime_constraint = runtime_constraint and (self.adjacency.get(node_2) is not None)
        if runtime_constraint:
            constraint = node_2 in self.adjacency[node_1]
            constraint = constraint and (node_1 in self.adjacency[node_2])
            constraint = constraint and (self.isGateway(node_1) or self.isGateway(node_2))
            if constraint:
                self.adjacency[node_1].remove(node_2)
                self.adjacency[node_2].remove(node_1)
            else:
                raise Exception('Invalid move')
        else:
            raise Exception('Some index is invalid')

    def terminalTest(self, node):
        winCondition = True
        for gateway in self.gateways:
            if len(self.adjacency[gateway]) > 0:
                winCondition = False
                break
        return self.isGateway(node) or winCondition

    def utility(self, node):
        if self.isGateway(node):
            return -1
        else:
            return 1

    def preference(self, node, visited_set):
        # returns sorted list of actions giving preference to not visited ones
        # and still more preference to gateways
        pref_list = []
        for action in self.adjacency[node]:
            if action in self.gateways:
                return [action]
            if action not in visited_set:
                pref_list.append(action)
        for action in visited_set:
            pref_list.append(action)
        return pref_list

    def gateway_ordering(self, node):
        sorted_list = []
        gateways = set()
        bfs_set = set()
        bfs_set.add(node)
        bfs_list = [node]
        while len(bfs_list) > 0:
            current = bfs_list.pop(0)
            if self.isGateway(current):
                if current not in gateways:
                    sorted_list.append(current)
                    gateways.add(current)
                if len(sorted_list) == len(self.gateways):
                    return sorted_list
            else:
                for neighbor in self.adjacency[current]:
                    if neighbor not in bfs_set:
                        bfs_list.append(neighbor)
                        bfs_set.add(neighbor)
        return sorted_list

    def isQuiescent(self, node):
        for neighbor in self.adjacency[node]:
            if self.isGateway(neighbor):
                return False
            count = 0
            for next_neighbor in self.adjacency[neighbor]:
                if self.isGateway(next_neighbor):
                    count += 1
                    if count > 1:
                        return False
        return True

    def cutoffTest(self, node, depth):
        max_depth = 11
        if depth >= max_depth and self.isQuiescent(node):
            return True
        else:
            return False

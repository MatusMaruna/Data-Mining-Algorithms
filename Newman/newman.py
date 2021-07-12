import pandas as pd
import numpy as np
import time
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--data', type=str, default=None, help='Edgelist file location')
parser.add_argument('--data_out', type=str, default=None, help='Output save location')
parser.add_argument('--communities', type=int, default=2)


def main():
    args = parser.parse_args()
    edgelist = pd.read_csv(args.data, sep=' ', header=None)
    edgelist = np.array(edgelist)
    start_time = time.time()
    communities = newman(edgelist, args.communities)
    for community in communities:
        community.sort()
    communities.sort()
    print(communities)
    if args.data_out is not None:
        f = open(args.data_out, "a")
        for i in range(len(communities)):
            f.write('Community' + str(i + 1) + ' :' + str(communities[i]) + '\n')
        f.close()
        print('Results written to file ' + str(args.data_out))
    print("Execution time:  %s seconds " % (time.time() - start_time))


def newman(dataset, num_communities):
    communities, dictionary, adjacency_matrix, neighbours = initilize(dataset)
    while len(communities) != num_communities:
        max_q = -np.inf
        for com1 in communities:
            temp_comm = communities.copy()
            temp_comm.remove(com1)
            for com2 in temp_comm:
                if comm_has_edge(com1, com2, adjacency_matrix,dictionary):
                    temp_merge = merge_comm(com1.copy(), com2.copy(), communities.copy())
                    q = calc_q(temp_merge, dataset, adjacency_matrix, dictionary, neighbours)
                    if q >= max_q:
                        max_q = q
                        max_q_com1 = com1
                        max_q_com2 = com2
        communities = merge_comm(max_q_com1, max_q_com2, communities)
    return communities


def initilize(dataset):
    communities = []
    dictionary = {}
    neighbours = {}
    id = 0
    for i in range(len(dataset)):
        if not contains(dataset[i][0],communities):
            neighbours[dataset[i][0]] = 0
            dictionary[dataset[i][0]] = id
            communities.append([dataset[i][0]])
            id += 1
        if not contains(dataset[i][1],communities):
            neighbours[dataset[i][1]] = 0
            dictionary[dataset[i][1]] = id
            communities.append([dataset[i][1]])
            id += 1
    adjacency_matrix = np.zeros((len(communities), len(communities)))
    for i in range(len(dataset)):
        adjacency_matrix[dictionary.get(dataset[i][0])][dictionary.get(dataset[i][1])] = 1
        adjacency_matrix[dictionary.get(dataset[i][1])][dictionary.get(dataset[i][0])] = 1
        neighbours[dataset[i][0]] = neighbours.get(dataset[i][0]) + 1
        neighbours[dataset[i][1]] = neighbours.get(dataset[i][1]) + 1
    return communities, dictionary, adjacency_matrix, neighbours


def contains(node, communities):
    for i in range(len(communities)):
        if node == communities[i][0]:
            return True

    return False


def has_edge(pid1, pid2, adjacency_matrix, dictionary):
    if (adjacency_matrix[dictionary.get(pid1)][dictionary.get(pid2)] == 1 or
            adjacency_matrix[dictionary.get(pid2)][dictionary.get(pid1)] == 1):
        return True
    else:
        return False


def comm_has_edge(com1, com2, adjacency_matrix, dictionary):
    for pid1 in com1:
        for pid2 in com2:
            if has_edge(pid1, pid2, adjacency_matrix, dictionary):
                return True
    return False


def merge_comm(com1, com2, communities):
    communities.remove(com1)
    communities.remove(com2)
    for node in com1:
        if node not in com2:
            com2 += com1
    communities.append(com2)
    return communities


def calc_q(communities, dataset, adjacency_matrix, dictionary, neighbours):
    m = len(dataset)*2
    a = 0
    e = 0
    for community in communities:
        sum = 0
        for i in community:
            for j in community:
                if has_edge(i, j, adjacency_matrix, dictionary):
                    sum += 1
        e += sum / (2 * m)
    for community in communities:
        sum = 0
        for node in community:
            sum += neighbours.get(node)
        a += (sum / (2 * m)) ** 2
    q = e/2 - a
    return q



if __name__ == "__main__":
    main()

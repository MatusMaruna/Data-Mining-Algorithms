import pandas as pd
import numpy as np
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--data', type=str, default=None, help='Edgelist file location')
parser.add_argument('--data_out', type=str, default=None, help='Output save location')
parser.add_argument('--err_tol', type=float, default=1e-06)
parser.add_argument('--max_iter', type=int, default=50)
parser.add_argument('--beta', type=float, default=0.85)


def main():
    args = parser.parse_args()
    edgelist = pd.read_csv(args.data, sep=' ', header=None)
    edgelist = np.array(edgelist)
    pr, dictionary = pagerank(edgelist, args.err_tol, args.max_iter, args.beta)
    if args.data_out is not None:
        f = open(args.data_out, "a")
        for node in dictionary.keys():
            f.write(str(node) + ' : ' + str(pr[dictionary.get(node)]) + '\n')
        f.close()
        print('Results written to file ' + str(args.data_out))
    for node in dictionary.keys():
        print(node, ' : ',pr[dictionary.get(node)])


def pagerank(dataset, err_tol, max_iter, beta):
    nodes,dictionary, transition_matrix = initilize(dataset)
    N = transition_matrix.shape[1]
    sums = transition_matrix.sum(axis=0)
    if 0 in sums:
        transition_matrix
        for i in np.where(sums == 0):
            transition_matrix[:, i] = 1/N
    iter = 0
    sum_diff = np.inf
    ranks = np.random.rand(N, 1)
    ranks = ranks / np.linalg.norm(ranks, 1)
    A = (beta * transition_matrix + (1.0 - beta) * np.ones((N,N))/N)

    while iter < max_iter and sum_diff > err_tol:
        old_ranks = ranks.copy()
        ranks = A.dot(ranks)
        sum_diff = np.sum(np.abs(ranks-old_ranks))
        iter += 1
    return ranks, dictionary


def initilize(dataset):
    nodes = []
    dictionary = {}
    neighbours = {}
    id = 0
    for i in range(len(dataset)):
        if not contains(dataset[i][0], nodes):
            dictionary[dataset[i][0]] = id
            nodes.append([dataset[i][0]])
            id += 1
        if not contains(dataset[i][1], nodes):
            dictionary[dataset[i][1]] = id
            nodes.append([dataset[i][1]])
            id += 1
        neighbours[dataset[i][0]] = np.array([])

    for i in range(len(dataset)):
        neighbours[dataset[i][0]] = np.append(neighbours.get(dataset[i][0]), dataset[i][1])

    transition_matrix = np.zeros((len(nodes), len(nodes)))
    for neighbourhood in neighbours.keys():
        for neighbour in neighbours.get(neighbourhood):
            transition_matrix[dictionary.get(neighbourhood)][dictionary.get(neighbour)] \
                = 1/len(neighbours.get(neighbourhood))
    return np.array(nodes), dictionary, transition_matrix.T

def contains(node, communities):
    for i in range(len(communities)):
        if node == communities[i][0]:
            return True

    return False

if __name__ == "__main__":
    main()

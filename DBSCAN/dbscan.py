import argparse
import pandas as pd
import numpy

parser = argparse.ArgumentParser()
parser.add_argument('--data', type=str, default=None, help='Location of the CSV dataset')
parser.add_argument('--epsilon', type=float, default=0.2)
parser.add_argument('--minpts', type=int, default=20)
parser.add_argument('--output', type=str, default=None, help='Location for output of the results')


def main():
    args = parser.parse_args()
    dataset = pd.read_csv(args.data, sep=',', header=None)
    dataset = numpy.array(dataset)
    eps = args.epsilon
    minpts = args.minpts
    clusterIds, c = dbscan(dataset, eps, minpts)
    clusters = []
    print('There are ' + str(c) + ' clusters!')
    for i in range(c):
        cluster = []
        clusters.append(cluster)
    for i in range(len(clusterIds)):
        clusters[clusterIds[i] - 1].append(i + 1)
    for i in range(len(clusters)):
        print('Cluster' + str(i+1) + ' :' + str(clusters[i]))
    if args.output is not None:
        f = open(args.output, "a")
        for i in range(len(clusters)):
            f.write('Cluster' + str(i + 1) + ' :' + str(clusters[i]) + '\n')
        f.close()
        print('Results written to file ' + str(args.output))


def dbscan(dataset, eps, minpts):
    cluster_ids = [0] * len(dataset)
    c = 0

    for i in range(0, len(dataset)):
        if not (cluster_ids[i] == 0):
            continue

        neighbour_points = range_query(dataset, i, eps)

        if len(neighbour_points) < minpts:
            cluster_ids[i] = -1
        else:
            c += 1
            cluster_ids = build_cluster(dataset, cluster_ids, i, neighbour_points, c, eps, minpts)
    return cluster_ids, c


def build_cluster(dataset, cluster_ids, point, neighbour_points, c, eps, minpts):
    cluster_ids[point] = c
    i = 0
    while i < len(neighbour_points):
        pointn = neighbour_points[i]
        if cluster_ids[pointn] == -1:
            cluster_ids[pointn] = c
        elif cluster_ids[pointn] == 0:
            cluster_ids[pointn] = c
            pointn_neighbour_points = range_query(dataset, pointn, eps)
            if len(pointn_neighbour_points) >= minpts:
                neighbour_points = neighbour_points + pointn_neighbour_points
        i += 1
    return cluster_ids


def range_query(dataset, point, eps):
    neighbours = []

    for i in range(0, len(dataset)):
        if numpy.linalg.norm(dataset[point] - dataset[i]) <= eps:
            neighbours.append(i)
    return neighbours

if __name__ == "__main__":
    main()

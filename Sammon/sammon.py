import numpy as np
import pandas as pd
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--data', type=str, default=None, help='')
parser.add_argument('--data_out', type=str, default="data_out.csv")
parser.add_argument('--magicfactor', type=float, default=0.35)
parser.add_argument('--iterations', type=int, default=50)
parser.add_argument('--initilization', type=str, default=None, help='')


def main():
    args = parser.parse_args()
    dataset = pd.read_csv(args.data, sep=',', header=None)
    dataset = np.array(dataset)
    out_name = args.data_out
    mfactor = args.magicfactor
    iterations = args.iterations
    projection = args.initilization

    data_out = sammon(dataset, projection, iterations, mfactor)
    np.savetxt(out_name,data_out, delimiter=',')


def sammon(data_matrix, initial_projection, max_iter, magic_factor):
    distance_matrix = calc_distance_matrix(data_matrix)
    if initial_projection is None:
        initial_projection = np.random.random((data_matrix.shape[0], 2))
    elif initial_projection.lower() == 'orthagonal':
        temp = data_matrix.copy()
        index = np.argmax(np.var(temp, axis=0, dtype=np.float32))
        column1 = temp[:, index]
        temp = np.delete(temp, index, 1)
        index = np.argmax(np.var(temp, axis=0, dtype=np.float32))
        column2 = temp[:, index]
        initial_projection = np.concatenate([column1.reshape(-1, 1),
                                             column2.reshape(-1, 1)], axis=1)

    sum_dist = 0.0
    for i in range(distance_matrix.shape[0]):
        for j in range(distance_matrix.shape[0]):
            if distance_matrix[i, j] < 1e-4:
                distance_matrix[i, j] = 1e-4
            sum_dist += distance_matrix[i, j]

    c = sum_dist / 2

    for i in range(max_iter):
        projection = initial_projection.copy()
        for p in range(distance_matrix.shape[0]):
            for q in range(2):
                sum_calc1 = 0.0
                sum_calc2 = 0.0
                for j in range(distance_matrix.shape[0]):
                    if j != p:
                        x = projection[p, 0] - projection[j, 0]
                        y = projection[p, 1] - projection[j, 1]
                        dist_pj = np.sqrt(x * x + y * y)

                        if dist_pj < 1e-4:
                            dist_pj = 1e-4

                        sum_calc1 += ((distance_matrix[p, j] - dist_pj) / (distance_matrix[p, j] * dist_pj)) * (
                                initial_projection[p, q] - initial_projection[j, q])
                        sum_calc2 += (1 / (distance_matrix[p, j] * dist_pj)) * ((distance_matrix[p, j] - dist_pj) - (
                                (np.power((initial_projection[p, q] - initial_projection[j, q]), 2) / dist_pj) * (
                                1 + ((distance_matrix[p, j] - dist_pj) / dist_pj))))
                delta_pq = (((-2 / c) * sum_calc1) / abs((-2 / c) * sum_calc2))
                initial_projection[p, q] -= magic_factor * delta_pq
    return initial_projection


def calc_distance_matrix(dataset):
    m, n = dataset.shape
    distance = np.sqrt(np.sum((dataset.reshape(m,1,n) - dataset.reshape(1,m,n))**2, axis=-1))
    return distance


if __name__ == "__main__":
    main()

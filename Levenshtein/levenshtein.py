import argparse
import numpy as np
import sys

sys.setrecursionlimit(10000)
parser = argparse.ArgumentParser()
parser.add_argument('--file_path', type=str, default=None, help='File location')
parser.add_argument('--c_del', type=int, default=2, help='Cost of deletion')
parser.add_argument('--c_ins', type=int, default=2, help='Cost of insertion')
parser.add_argument('--c_sub', type=int, default=1, help='Cost of substitution')


class Levenshtein:

    def main(self, file_path, c_del, c_ins, c_sub):
        file = np.genfromtxt(file_path, delimiter="\n", dtype=None, encoding=None)
        self.c_del = c_del
        self.c_ins = c_ins
        self.c_sub = c_sub
        self.a = file[0]
        self.b = file[1]
        self.memory = {}
        print(self.dist(self.a, self.b))

    def lev(self, i, j):
        if i == 0:
            return j
        if j == 0:
            return i
        if self.a[i - 1] == self.b[j - 1]:
            c_sub = 0
        else:
            c_sub = 1
        arg_del = (i - 1, j)
        if arg_del not in self.memory:
            self.memory[arg_del] = self.lev(*arg_del)
        arg_ins = (i, j - 1)
        if arg_ins not in self.memory:
            self.memory[arg_ins] = self.lev(*arg_ins)
        arg_sub = (i - 1, j - 1)
        if arg_sub not in self.memory:
            self.memory[arg_sub] = self.lev(*arg_sub)

        lev_ret = min(
            [self.memory[arg_del] + self.c_del, self.memory[arg_ins] + self.c_ins, self.memory[arg_sub] + c_sub])

        return lev_ret

    def dist(self, a, b):
        return self.lev(len(a), len(b))


if __name__ == "__main__":
    args = parser.parse_args()
    Levenshtein().main(args.file_path, args.c_del, args.c_ins, args.c_sub)


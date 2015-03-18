#!/usr/bin/python


def solve(D, T, a, b):
        ans = 1000000000
        if (D < 1000000000):
                return D[a][b];
        if (a == b):
                return 1
        if (T[a] == T[b]):
                return 1

        for i in xrange(a,b):
                if (T[a] == T[i]):
                        temp = 1 + solve(D, T, a+1, b)
                        if (temp < ans):
                                ans = temp
        D[a][b] = ans
        return ans

with open("input.txt","r") as f:
        x = int(f.readline())
        for i in xrange(x):
                T = f.readline().rstrip()
                D = [[1000000000 for c in xrange(len(T))] for d in xrange(len(T))]
                print solve(D, T, 0, len(T)-1)

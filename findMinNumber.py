#!/bin/python3

# https://www.hackerrank.com/contests/w30/challenges/find-the-minimum-number

import sys

n = int(input().strip())


def findMinNumber(i):
    if i == 2:
        return "min(int, int)"
    else:
        return "min(int, {})".format(findMinNumber(i - 1))


print(findMinNumber(n))

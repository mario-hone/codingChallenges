#!/bin/python3

import sys

n = int(input().strip())


def findMinNumber(i):
    if i == 2:
        return "min(int, int)"
    else:
        return "min(int, {})".format(findMinNumber(i - 1))


print(findMinNumber(n))

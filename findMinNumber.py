#!/bin/python3

import sys

n = int(input().strip())


def findMinNumber(i):
    if i == 2:
        return "min(int, int)"
    else:
        print("min(int, {})".format(findMinNumber(i - 1)))


findMinNumber(n)

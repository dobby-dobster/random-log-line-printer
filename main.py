#!/usr/bin/env python

import random

def GenerateRandomNumbers():
    RandomNumbers = []

    for i in random.sample(range(0, 10), 5):
        RandomNumbers.append(i)
    print("Random line numbers: {}").format(RandomNumbers)
    return RandomNumbers

def main():
    RandomNumbers = GenerateRandomNumbers()
    count = 0
    for line in open("log.txt").xreadlines(  ):
        count += 1
        for item in RandomNumbers:
            if count == item:
                print(line)
                print(item)
if __name__ == '__main__':
    main()

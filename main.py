#!/usr/bin/env python

import random

def GenerateRandomNumbers():
    RandomNumbers = []

    for i in random.sample(range(1, 11), 5):
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
                print("Line number {0}: {1}".format(item, line))
                
if __name__ == '__main__':
    main()

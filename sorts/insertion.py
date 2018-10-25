"""
Insertion Sort

Performance Time: O(n**2)
Space complexity: O(n)
"""
import random


def insertion(collection):
    # We start loop at second element since the first item is already sorted
    for j in range(1, len(collection)):
        key = collection[j]
        i = j
        while (i > 0) and collection[i-1] > key:
            collection[i] = collection[i-1]
            i -= 1
        collection[i] = key
    return collection


if __name__ == '__main__':
    # n = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    # n = [-54, -26, -93, -17, -77, -44, -55, -20]
    n = [random.randrange(1, 1000) for _ in range(0, 10000)]
    # print(n)
    #for j in range(i)
    #    n.append(random())
    insertion(n)

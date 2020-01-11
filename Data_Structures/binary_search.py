from time import time
from typing import List
def contains(collection: List[int] , target: int):
    """Check wether the target element is in collections"""
    return target in collection

def bs_contains(ordered: List[int], target: int):
    """Binary search algorithm."""
    low = 0
    high = len(ordered) - 1
    while low <= high:
        mid = int((low + high) / 2)
        if ordered[mid] == target:
            # if element already exists, then you want to insert the element next to the element
            return mid
        elif ordered[mid] > target:
            high = mid - 1
        else:
            low = mid + 1
    return -(low + 1)

def insertInPlace(ordered: List[int], target: int):
    idx = bs_contains(ordered, target)
    ordered = list(ordered)
    if idx < 0:
        ordered.insert(-(idx + 1), target)
        return
    ordered.insert(idx, target)
    # for idx in range(len(ordered)):
    #     if ordered[idx] < target:
    #         ordered.insert(idx + 1, target)
    # ordered.append(target)


def performance():
    """Check the performance of various algorithms."""
    
    n = 1024
    while n < 500000000:
        sorted = range(n)
        t1 = time()
        insertInPlace(sorted, n + 1)
        t2 = time()
        print(n, (t2-t1) * 1000)
        n *= 2

if __name__ == "__main__":
    performance()    

from Heap import Heap
import heapq
'''
Q: Find smallest k elements form an unsorted array of size n
'''

# Solution 1: O(n + klogn)
#   1. heapify the array to form a min heap of size n, O(n)
#   2. pop out its first k smallest element(heapify k time), O(klogn)
def top_k_smallest_1(arr, k):
    if not arr:
        return []

    # build a min heap wrt the given array
    heap = Heap(arr)

    # pop out the first k smallest elements from the heap
    rs = []
    for i in range(k):
        rs.append(heap.heappop())

    return rs

# Solution 2: O(k + (n-k)logK)
#   1. heapify the first k elements to form a max heap of size k, O(k)
#   2. iterate over the rest n - k elements one by one. When transverse a new element, compare with the largest
#      element of the previous k smallest candidates: O((n-k)logk)
#           2.1 new element > top ignore
#           2.2 new element < top pop out top and push new element into the heap
def top_k_smallest_2(arr, k):
    if not arr:
        return []

    # change the first k elements to negative number and build a min heap wrt them
    rs = [-i for i in arr[0:k]]
    heap = Heap(rs)

    # iterate over the rest n - k elements one by one
    for i in range(k, len(arr)):
        if -arr[i] > heap.get_top():
            heap.heappop()
            heap.heappush(-arr[i])

    return [-i for i in heap.get_heap()]

# heapq version
def top_k_smallest_3(arr, k):

    if not arr or len(arr) == 0:
        return []

    rs = [-i for i in arr[0:k]]
    # invoke heapify function in file heapq.
    heapq.heapify(rs)

    for i in range(k+1, len(arr)):
        if arr[i] < -rs[0]:
            heapq.heappop(rs)
            heapq.heappush(rs, -arr[i])

    return [-i for i in rs]


arr = [6, 8, 9, 0, 1, 5, 4, 11, 15, 2, -1, 2]
x = top_k_smallest_2(arr, 5)
print(x)


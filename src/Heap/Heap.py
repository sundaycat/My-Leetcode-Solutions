"""
Implement a min heap(items in heap can be tuples)
Note: python use default sorting for tuples, that is it only compares the 1st element of the tuple
"""
class Heap(object):

    def __init__(self, arr=[]):
        self.__heap = list(arr)
        self.__size = len(arr)
        self.__build_min_heap()

    def get_top(self):
        if not self.__heap:
            return None

        return self.__heap[0]

    # return True if the heap is empty
    def is_empty(self):
        return self.__size == 0

    def get_heap(self):
        return not self.__heap

    def __build_min_heap(self):
        # start from the level that is one level up of the leave
        n = len(self.__heap) // 2 - 1
        for idx in range(n, -1, -1):
            self.__sift_down(idx)

    def heappush(self, item):
        self.__heap.append(item)
        self.__sift_up(len(self.__heap) - 1)
        self.__size += 1

    def heappop(self):
        # return None if heap is empty
        if not self.__heap:
            return None

        # exchange the position of the top and last item
        last = len(self.__heap) - 1
        self.__heap[0], self.__heap[last] = self.__heap[last], self.__heap[0]

        # pop out the smallest element and heapify
        min_item = self.__heap.pop()
        self.__size -= 1
        self.__sift_down(0)

        return min_item

    # heapify from top down
    def __sift_down(self, curIdx):

        heap = self.__heap
        smaller = curIdx
        while curIdx < len(heap):

            left = (curIdx << 1) + 1
            right = (curIdx << 1) + 2

            if left < len(heap) and heap[left] < heap[curIdx]:
                smaller = left
            if right < len(heap) and heap[right] < heap[smaller]:
                smaller = right

            # break out the loop if the curIdx is smaller than its child
            if smaller == curIdx: break

            # exchange the value of curIdx with smaller element of its child
            heap[curIdx], heap[smaller] = heap[smaller], heap[curIdx]
            curIdx = smaller

    # heapify from the bottom up
    def __sift_up(self, curIdx):

        heap = self.__heap
        while curIdx >= 0:

            parent = (curIdx - 1) >> 1
            if parent >= 0 and heap[parent] > heap[curIdx]:
                heap[parent], heap[curIdx] = heap[curIdx], heap[parent]

            curIdx = parent

    '''
    heap sort algorithm:
        1. build a min heap with the current array
        2. find min element and swap it with the last element of the heap
        3. discard last element(min element) from heap and decrease the heap size by 1
        4. Apply the min_heapify(new root violate the min heap property but children are still min heap)
    '''
    def heap_sort(self):
        rs = []
        while self.__size > 0:
            item = self.heappop()
            rs.append(item)

        return rs


arr = [0, 2, 5, 6, 8, 9, -1]
heap = Heap(arr)
rs = heap.heap_sort()
print(rs)

arr1 = [(5, 0, 0), (4, 0, 1), (3, 1, 0)]
heap1 = Heap(arr1)

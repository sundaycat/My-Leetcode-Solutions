from Heap import Heap

'''
Q: Merger K sorted arrays, n is the number of all elements in k arrays.

Solution: O(K + nlogk)
    Step 1: create a min heap, push the first element of each array into the heap, O(k)
    Step 2: Each time pop an element fromm the heap, and then push the next element into the heap O(nlogk)
    
Note: python use default sorting for tuples, that is it only compares the 1st element of the tuple
'''

# 思路：将当前k个队列中各自的最小值放入heap中，并选出它们之中的最小值。
def merge_sorted_arrays(arr_of_arrs):

    if not arr_of_arrs:
        return arr_of_arrs

    # use the first element of each list to form a min heap of size k
    heap = Heap()
    for i in range(len(arr_of_arrs)):
        # create a tuple records the value, row index and column index of the current element
        item = (arr_of_arrs[i][0], i, 0)
        heap.heappush(item)

    # each time pop an element out of the heap and then push the next element into the heap
    rs = []
    while not heap.is_empty():
        value, row, col = heap.heappop()
        rs.append(value)

        if col + 1 < len(arr_of_arrs[row]):
            new_item = (arr_of_arrs[row][col + 1], row, col + 1)
            heap.heappush(new_item)

    return rs


x = [[1, 2, 3], [1, 4, 9, 10], [0, 2, 6, 8]]
y = merge_sorted_arrays(x)
print(y)
from Heap import Heap
import heapq

'''
Given k sorted integer arrays, pick k elements (one element from each of sorted arrays), what is the smallest range.

Solution: Always maintain a min and max value 
1. use the 1st element of each list to form a min heap of size k
2. maintain a max value of the heap
3. for any incoming new item, there are two possible cases that might cause to update the smallest range:
    (1) 【min 2nd new_item max】
    (2) 【min {2nd max】 new_item}
    
NOTE: min and new_item are always come from the same list, so min < new_item.
'''
def find_smallest_range(arr_of_arrs):

    if not arr_of_arrs:
        return arr_of_arrs

    # use the first element of each list to form a min heap of size k
    heap = Heap()
    r_rng = max_val = float('-inf')
    for i in range(len(arr_of_arrs)):

        # keep track of the max value of the min heap
        if arr_of_arrs[i][0] > max_val:
            r_rng = max_val = arr_of_arrs[i][0]

        # create a tuple records the value, row index and column index of the current element
        item = (arr_of_arrs[i][0], i, 0)

        # push the tuple into heap
        heap.heappush(item)

    # pop out the min in heap and initialize the l_rng
    l_rng, row, col = heap.heappop()
    rng = r_rng - l_rng
    while col + 1 < len(arr_of_arrs[row]):

        new_item = (arr_of_arrs[row][col + 1], row, col + 1)
        heap.heappush(new_item)

        # 始终记录heap中的最大值
        if max_val < new_item[0]:
            max_val = new_item[0]

        # ps_l_rng 为当前heap的最小值, 也是可能的左边界
        # [min 2nd {new_item max}] or [min {2nd max] new_item}
        ps_l_rng, row, col = heap.heappop()
        if rng > max_val - ps_l_rng:
            rng = max_val - ps_l_rng
            l_rng = ps_l_rng
            r_rng = max_val

    return [l_rng, r_rng]

'''
# use heapq class
def find_smallest_range_1(arr_of_arrs):

    heap = []
    r_rng = max_val = float('-inf')
    for i in range(len(arr_of_arrs)):
        if arr_of_arrs[i][0] > max_val:
            max_val = arr_of_arrs[i][0]

        item = (arr_of_arrs[i][0], i, 0)
        heapq.heappush(heap, item)

    l_rng, row, col = heapq.heappop(heap)
    rng = max_val - l_rng
    while col + 1 < len(arr_of_arrs[row]):
        new_item = (arr_of_arrs[row][col+1], row, col+1)
        heapq.heappush(heap, new_item)

        if new_item[0] > max_val:
            max_val = new_item[0]

        min_val, row, col = heapq.heappop(heap)
        if rng > max_val - min_val:
            rng = max_val - min_val
            l_rng = min_val
            r_rng = max_val

    return [l_rng, r_rng]
'''

x = [[1,4],[2,5],[8,10]]
x1 = [[4,10,11],[1,3,7,11],[6,9,16],[4,10]]
y = find_smallest_range_1(x1)
print(y)

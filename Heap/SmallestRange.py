from Heap import Heap
import heapq

'''
Q: Given k sorted integer arrays, pick k elements (one element from each of sorted arrays), what is the smallest range.

Solution: Always maintain a min and max value 
1. use the 1st element of each list to form a min heap of size k
2. maintain a max and min value of the heap
3. for any incoming item, there are 3 possible cases that might cause to update or not update the smallest range:
    (1) New item is the min element of the current heap
        1.1 new_item > pre_min 2nd 3rd ... max      not update
        1.2 pre_min  < new_item 2nd 3rd ... max     update
    (2) New item is neither the min nor the max of the current heap
        pre_min 2nd 3rd ... new_item ... max        not update
    (3) New item is the max element of the current heap
        3.1 {pre_min [2nd ... new_item] pre_max}    update
        3.2 {pre_min [2nd ... pre_max} new_item]    depends
            
NOTE: min and new_item are always come from the same list, so min < new_item.
      the new min or max doesn't have to smaller or larger than than pre_min or pre_max
'''
def find_smallest_range(arr_of_arrs):

    if not arr_of_arrs:
        return []

    # use the first element of each list to form a min heap of size k
    heap = Heap()
    max_val = float('-inf')
    for i in range(len(arr_of_arrs)):

        # keep track of the max value of the min heap
        if arr_of_arrs[i][0] > max_val:
            max_val = arr_of_arrs[i][0]

        # create a tuple records the value, row and column index of the current element
        new_item = (arr_of_arrs[i][0], i, 0)

        # push the tuple into heap
        heap.heappush(new_item)

    # pop out the min element in heap(keep track of min in current heap)
    min_val, row, col = heap.heappop()
    # initialize the smallest range
    rng = max_val - min_val
    # l_rng and r_rng use to record smallest range of the arrays
    l_rng = min_val; r_rng = max_val;
    while col + 1 < len(arr_of_arrs[row]):

        new_item = (arr_of_arrs[row][col + 1], row, col + 1)
        heap.heappush(new_item)

        # keep track the max value in heap
        if max_val < new_item[0]:
            max_val = new_item[0]

        # Each time, we push a new item into the heap might cause a change in the smallest range, so we need to compare
        # the new range in current heap with the pre_range and update the smallest heap accordingly
        min_val, row, col = heap.heappop()
        if rng > max_val - min_val:
            rng = max_val - min_val
            l_rng = min_val
            r_rng = max_val

    return [l_rng, r_rng]

# use heapq version
def find_smallest_range(arr_of_arrs):

    if not arr_of_arrs or len(arr_of_arrs) == 0:
        return []

    heap = []
    max_val = float('-inf')
    for i in range(0, len(arr_of_arrs)):
        if arr_of_arrs[i][0] > max_val:
            max_val = arr_of_arrs[i][0]

        new_item = (arr_of_arrs[i][0], i, 0)
        heapq.heappush(heap, new_item)

    min_val, row, col = heapq.heappop(heap)
    l_rng = min_val; r_rng = max_val
    rng = max_val - min_val
    while col + 1 < len(arr_of_arrs[row]):
        new_item = (arr_of_arrs[row][col + 1], row, col + 1)
        if new_item[0] > max_val:
            max_val = new_item[0]

        heapq.heappush(heap, new_item)
        min_val, row, col = heapq.heappop(heap)
        if rng > max_val - min_val:
            rng = max_val - min_val
            l_rng = min_val
            r_rng = max_val

    return [l_rng, r_rng]

x = [[1,4],[2,5],[8,10]]
x1 = [[4,10,11],[1,3,7,11],[6,9,16],[4,10]]
y = find_smallest_range(x1)
print(y)



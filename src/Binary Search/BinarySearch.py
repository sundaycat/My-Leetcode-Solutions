def k_closest(array, target, k):
    """
    input: int[] array, int target, int k
    return: int[]
    """
    if len(array) == 0 or k <= 0:
        return -1

    # located the elements that is closest to the target
    left, right, index = 0, len(array) - 1, -1
    while left + 1 < right:
        mid = (left + right) // 2
        if array[mid] > target:
            right = mid
        elif array[mid] < target:
            left = mid
        else:
            index = mid
            break

    if index == -1:
        index = left if abs(array[left] - target) < abs(array[right] - target) else right

    # check the neighbor of x k-1 time to pick the k closest elements
    left, right = index, index + 1
    i = 1
    # Under the following condition, we make right = right + 1
    # target is at the left most of the array
    # left element is closer to target than the right element
    while i < k:
        if left == 0 or (right < len(array) and abs(array[left - 1] - target) > abs(array[right] - target)):
            right = right + 1
        else:
            left = left - 1
        i = i + 1
    return array[left: right]

def total_occurrence(self, array, target):
    """
    input: int[] array, int target
    return: int
    """
    # write your solution here
    if len(array) == 0:
        return 0

    # find the first occurrence of target
    left, right, first = 0, len(array) - 1, -1
    while left < right - 1:
        mid = (left + right) / 2
        if array[mid] < target:
            left = mid
        else:
            right = mid

    if array[left] == target:
        first = left

    if first != left and array[right] == target:
        first = right

    # find the last occurrence of target
    left, right, last = 0, len(array) - 1, -1
    while left < right - 1:
        mid = (left + right) / 2
        if array[mid] > target:
            right = mid
        else:
            left = mid

    if array[right] == target:
        last = right

    if last != right and array[left] == target:
        last = left

    count = 0;
    if first != -1 and last != -1:
        count = last - first + 1

    return count

def search(matrix, target):
    if matrix is None or len(matrix) == 0:
        return None

    row, col = len(matrix), len(matrix[0])
    left, right = 0, row * col - 1

    while left <= right:

        mid = (left + right) // 2
        rowIdx, colIdx = mid // col, mid % col

        if matrix[rowIdx][colIdx] > target:
            right = mid - 1
        elif matrix[rowIdx][colIdx] < target:
            left = mid + 1
        else:
            return (mid // col, mid % col)

    return None


def last_occurence(arr, target):

    if not arr or len(arr) == 0:
        return -1

    left, right = 0, len(arr) - 1
    while left + 1 < right:
        mid = (left + right) // 2
        if arr[mid] > target:
            right = mid
        else:
            left = mid

    if arr[right] == target:
        return right
    if arr[left] == target:
        return left

    return -1
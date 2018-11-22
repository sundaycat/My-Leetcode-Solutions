# Q1: Find the target number in a sorted int array
def binary_search(array, target):
    # corner case
    if arr is None or len(arr) == 0:
        return None

    left = 0
    right = len(array) - 1

    # if mid > target, then [ )
    # if mid < target, then ( ]
    # if mid == target, then return mid
    while left <= right:
        mid = (left + right) // 2
        if array[mid] > target:
            right = mid - 1
        elif array[mid] < target:
            left = mid + 1
        else:
            return mid

    return None

# Q2: Apply binary search in 2D space
def binary_search_2d(matrix, target):
    if matrix is None or len(matrix) == 0:
        return None

    row, col = len(matrix), len(matrix[0])
    left, right = 0, row * col - 1

    while left <= right:
        # find the mid position and calculate its corresponding row, col index
        mid = (left + right) // 2
        rowIdx, colIdx = mid // col, mid % col

        if matrix[rowIdx][colIdx] > target:
            right = mid - 1
        elif matrix[rowIdx][colIdx] < target:
            left = mid + 1
        else:
            return (rowIdx, colIdx)

    return None


# Q3: Find the element in the array that is closest to the target number
def binary_search_cloest(array, target):
    if not array or len(array) == 0:
        return None

    left, right = 0, len(array) - 1
    # change end condition to left + 1 < right
    while left < right - 1:
        mid = (left + right) // 2
        # have to keep mid element for next iteration
        if array[mid] > target:
            right = mid
        elif array[mid] < target:
            left = mid
        else:
            return mid

    # post-processiong the last two left elements
    index = left if abs(array[left] - target) < abs(array[right] - target) else right
    return index


# Q4: Find the index of the first occurrence of an element
def first_occurence(array, target):
    if not array or len(array) == 0:
        return -1

    left, right = 0, len(array) - 1
    while left < right - 1:
        mid = (left + right) // 2
        if array[mid] < target:
            left = mid
        else:
            right = mid

    # post-processing
    if array[left] == target:
        return left
    if array[right] == target:
        return right

    return -1


# Q5: find the index of the last occurrence of an element
def last_occurence(array, target):
    if not array or len(array) == 0:
        return -1

    left, right = 0, len(array) - 1
    while left < right - 1:
        mid = (left + right) // 2
        if array[mid] > target:
            right = mid
        else:
            left = mid

    # post-processing, fist check right and then left
    if array[right] == target:
        return right
    if array[left] == target:
        return left

    return -1


# Q6 Find peak element, assume the head and tail is negative infinity
def find_peak(arr):
    if not arr or len(arr) == 0:
        return -1

    left, right = 0, len(arr) - 1
    while left < right - 1:
        mid = (left + right) // 2
        # if arr[mid] > arr[mid - 1] and arr[mid] > arr[mid + 1]:
        if arr[mid - 1] < arr[mid] > arr[mid + 1]:
            return mid
        elif arr[mid] < arr[mid + 1]:
            left = mid + 1
        else:
            right = mid - 1

    return left if arr[left] >= arr[right] else right

# Q7: find K closest elements to the target
def k_closest(arr, k, target):

    if not arr or len(arr) == 0:
        return None

    # located the elements that is closest to the target
    left, right, closest = 0, len(arr) - 1, -1
    while left < right - 1:
        mid = (left + right) // 2
        if arr[mid] > target:
            right = mid
        elif arr[mid] < target:
            left = mid
        else:
            closest = mid
            break

    if closest == -1:
        closest = left if abs(arr[left] - target) < abs(arr[right] - target) else right

    # check the neighbor of closest k-1 times to pick the k closest elements
    # Under the following condition, we make left = left + 1
    # 1. closest element is at the right most of the array
    # 2. right element is closer to target than the left element
    left, right = closest, closest
    while k > 1:
        # right == len(arr) - 1 also guarantee that the right index won't be out of boundary
        if right == len(arr) - 1 or (left > 0 and abs(arr[left - 1] - target) <= abs(arr[right + 1] - target)):
            left -= 1
        else:
            right += 1

        k -= 1

    return arr[left:right + 1]

def total_occurrence(array, target):

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

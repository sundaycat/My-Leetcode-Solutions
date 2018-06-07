# merge sort
def merge(arr1, arr2):
    merge_arr = []

    idx1, idx2 = 0, 0
    while idx1 < len(arr1) and idx2 < len(arr2):
        if arr1[idx1] < arr2[idx2]:
            merge_arr.append(arr1[idx1])
            idx1 = idx1 + 1
        else:
            merge_arr.append(arr2[idx2])
            idx2 = idx2 + 1

    if idx1 == len(arr1):
        merge_arr.extend(arr2[idx2:])

    if idx2 == len(arr2):
        merge_arr.extend(arr1[idx1:])

    return merge_arr

def merge_sort(arr):
    if not arr or len(arr) == 0:
        return None

    if len(arr) == 1:
        return arr
    else:
        mid = len(arr) // 2
        l_arr = merge_sort(arr[:mid]) # [0, mid)
        r_arr = merge_sort(arr[mid:]) # [mid, end]
        return merge(l_arr, r_arr)

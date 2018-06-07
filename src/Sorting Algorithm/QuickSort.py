from random import randrange

'''
start: the starting point of the sub-array 
end: the ending point of the sub-array. End = len(sub-array). [start, end)
pivot: the index of the pivot element.
'''
def partition(arr, start, end, pivot):
    # swap pivot to the first element of the array
    arr[start], arr[pivot] = arr[pivot], arr[start]
    i = start
    # end is larger than the largest index one unit
    for j in range(start + 1, end):
        if arr[j] < arr[start]:
            # find the element that larger than pivot and swap them with the (i + 1)th element
            arr[j], arr[i + 1] = arr[i + 1], arr[j]
            i = i + 1

    # swap the pivot with last element that smaller than pivot.
    arr[i], arr[start] = arr[start], arr[i]
    return i

# end is one larger than the index of last element
def quick_sort(arr, start, end):

    if start < end:
        idx = randrange(start, end)
        pivot = partition(arr, start, end, idx)
        quick_sort(arr, start, pivot)
        quick_sort(arr, pivot + 1, end)

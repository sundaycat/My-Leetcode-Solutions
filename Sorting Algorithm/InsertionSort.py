def insertion_sort(arr):
    for j in range(1, len(arr)):
        i = j - 1
        current = arr[j]
        while i >= 0 and arr[i] > current:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
            i = i - 1
        arr[i + 1] = current

    return None

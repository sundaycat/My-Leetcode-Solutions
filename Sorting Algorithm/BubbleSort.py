def bubble_sort(arr):
    # outer index controls the total number of iterations, its index range from len(arr) - 1 to 1
    for outer in range(len(arr) - 1, 0, -1):
        # inner loop conducts the swap operation, its index range from 0 to outer - 1
        for inner in range(outer):
            if arr[inner] > arr[inner + 1]:
                arr[inner], arr[inner + 1] = arr[inner + 1], arr[inner]

    return None
def insertion_sort(arr):
    for j in range(1, len(arr), 1):
        i = j - 1
        while i >= 0 and arr[i + 1] < arr[i]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
            i = i - 1


temp = [8, 2, 4, 9, 3, 6]
insertion_sort(temp)
print(temp)
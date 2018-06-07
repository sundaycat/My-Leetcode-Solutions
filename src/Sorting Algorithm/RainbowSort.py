"""
Use two-pass algorithm to swap -1 to leftmost and 1 to rightmost.
[0,i): -1
[i,j]: 0
[k: ]: 1
"""
def rainbow_sort(array):
    # red -1, green 0, blue 1
    i, j, k = 0, 0, len(array) - 1
    while j <= k:
        if array[j] == -1:
            array[i], array[j] = array[j], array[i]
            i = i + 1
            j = j + 1
        elif array[j] == 0:
            j = j + 1
        else:
            array[k], array[j] = array[j], array[k]
            k = k - 1
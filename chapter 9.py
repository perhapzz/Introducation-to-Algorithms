# Randomized selected
def partition(array, low, high):
    pivot = array[low]
    while low < high:
        while low < high and array[high] > pivot:
            high -= 1
        array[low] = array[high]
        while low < high and array[low] < pivot:
            low += 1
        array[high] = array[low]
    array[low] = pivot
    return low

def randomized_selected(array, low, high, i):
    pos = partition(array, low, high)
    if pos == i:
        return array[pos]
    elif pos > i:
        return randomized_selected(array, low, pos - 1, i)
    else:
        return randomized_selected(array, pos + 1, high, i)


if __name__ == '__main__':
    array = list(map(int, input().strip().split()))
    i = int(input())
    print(randomized_selected(array, 0, len(array) - 1, i))

# 2 8 7 1 3 5 6 4
# 1 2 3 4 5 6 7 8
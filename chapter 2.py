# P10\ 2.1-2
def InsertSort(list, reverse = False):
    for i in range(1, len(list)):
        key = list[i]
        j = i - 1
        if reverse:
            while list[j] < key and j >= 0:
                list[j + 1] = list[j]
                j = j - 1
        else:
            while list[j] > key and j >= 0:
                list[j + 1] = list[j]
                j = j - 1
        list[j + 1] = key

# 2.3-4
def InsertSort_recur(list, n, reverse = False):
    if n > 0:
        InsertSort_recur(list, n - 1, reverse)
        key = list[n]
        i = n - 1
        if reverse:
            while list[i] < key and i >= 0:
                list[i + 1] = list[i]
                i -= 1
        else:
            while list[i] > key and i >= 0:
                list[i + 1] = list[i]
                i -= 1
        list[i + 1] = key

# 2.1-3
def LinearSearch(list, x):  # if cannot find x then return -1
    for i in range(len(list)):
        if list[i] == x:
            return i
    return -1

# 2. 3-5
def BinarySearch(list, x):
    left = 0
    right = len(list) - 1
    while left <= right:
        mid = int((left + right) / 2)
        if list[mid] > x:
            right = mid - 1
        else:
            left = mid + 1
    return right

# P17
def Merge(list, p, q, r):  # list[p..q] and list[q+1..r] are both sorted, merge them into one list
    n1 = q - p + 1
    n2 = r - q
    # let list[1..n1+1] and list[1..n2+1] be new arrays
    L = []
    R = []
    for i in range(n1):
        L.append(list[p + i])
    for i in range(n2):
        R.append(list[q + i + 1])
    L.append(float("inf"))
    R.append(float("inf"))
    i = 0
    j = 0
    for k in range(p, r + 1):
        if L[i] < R[j]:
            list[k] = L[i]
            i += 1
        else:
            list[k] = R[j]
            j += 1

# 2.3-2
def Merge_2(list, p, q, r):
    n1 = q - p + 1
    n2 = r - q
    # let list[1..n1+1] and list[1..n2+1] be new arrays
    L = []
    R = []
    for i in range(n1):
        L.append(list[p + i])
    for i in range(n2):
        R.append(list[q + i + 1])
    i = 0
    j = 0
    k = p
    while i < len(L) and j < len(R):
        if L[i] < R[j]:
            list[k] = L[i]
            i += 1
        else:
            list[k] = R[j]
            j += 1
        k += 1
    while i < len(L):
        list[k] = L[i]
        i += 1
        k += 1
    while j < len(R):
        list[k] = R[j]
        j += 1
        k += 1

def MergeSort(list, p, q):  # first call MergeSort(list, 0, len(list) - 1)
    if p < q:
        mid = int((p + q) / 2)
        MergeSort(list, p, mid)
        MergeSort(list, mid + 1, q)
        Merge_2(list, p, mid, q)

# 2-2
def BubbleSort(list):
    for i in range(1, len(list)):
        for j in reversed(range(i, len(list))):
            if list[j - 1] > list[j]:
                list[j - 1], list[j] = list[j], list[j - 1]

def main():
    pass

if __name__ == '__main__':
    list = list(map(int, input().strip().split()))
    BubbleSort(list)
    print(list)



# 6 2 1 3 4 7 9 0 8 5
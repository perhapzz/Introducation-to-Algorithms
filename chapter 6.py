# Heap Sort
def parent(i):
    return int(i / 2)

def left(i):
    return i * 2

def right(i):
    return i * 2 + 1

class Heap:
    data = []   # 堆的列表不是从0开始，而是从1开始
    size = 0

    def __init__(self, data = []):
        self.data = data[:]
        self.data.insert(0, 0)
        self.size = len(data)

    def Output(self):
        if self.size < 1:
            print("None")
        else:
            print(self.data[1:])

    def MaxHeapify(self, i):
        key = self.data[i]
        j = i * 2
        while j <= self.size:
            if j + 1 <= self.size and self.data[j + 1] > self.data[j]:
                j += 1
            if self.data[j] > key:
                self.data[i] = self.data[j]
                i = j
                j = j * 2
            else:
                break
        self.data[i] = key

    def BuildMaxHeap(self):
        for i in reversed(range(1, int(self.size / 2) + 1)):
            self.MaxHeapify(i)

    def HeapSort(self):
        self.BuildMaxHeap()
        for i in reversed(range(2, self.size + 1)):
            self.data[i], self.data[1] = self.data[1], self.data[i]
            self.size -= 1
            self.MaxHeapify(1)

    def HeapMaximum(self):
        return self.data[1]

    def HeapExtractMax(self):
        if self.size < 1:
            return None
        res = self.data[1]
        self.data[1] = self.data[self.size]
        self.size -= 1
        self.MaxHeapify(1)
        return res

    def HeapIncreaseKey(self, i, key):
        if self.data[i] > key:
            print("new key is smaller than current key")
            return None
        j = int(i / 2)
        while j > 0:
            if self.data[j] < key:
                self.data[i] = self.data[j]
                i = j
            else:
                break
        self.data[i] = key

    def MaxHeapInsert(self, key):
        self.size = self.size + 1
        self.data.append(float("-inf"))
        self.HeapIncreaseKey(self.size, key)


if __name__ == '__main__':
    array = list(map(int, input().strip().split()))
    A = Heap(array)
    # for i in array:
    #     A.MaxHeapInsert(i)
    A.BuildMaxHeap()
    A.Output()


# 4 1 3 2 16 9 10 14 8 7
# 4 1 3 14 16 9 10 2 8 7
# 16 14 10 8 7 9 3 2 4 1

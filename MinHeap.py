class MinHeap:
    def __init__(self):
        self.heapList = [0]
        self.currSize = 0

    def getMin(self):
        return self.heapList[1]

    def Up(self, i):
        while i // 2 > 0:
            k = i // 2
            if self.heapList[i] < self.heapList[k]:
                tmp = self.heapList[k]
                self.heapList[k] = self.heapList[i]
                self.heapList[i] = tmp
            i = i // 2

    def insert(self, k):
        self.heapList.append(k)
        self.currSize = self.currSize + 1
        self.Up(self.currSize)

    def Down(self, i):
        while (i * 2) <= self.currSize:
            mc = self.minChild(i)
            if self.heapList[i] > self.heapList[mc]:
                tmp = self.heapList[i]
                self.heapList[i] = self.heapList[mc]
                self.heapList[mc] = tmp
            i = mc

    def minChild(self, i):
        if i * 2 + 1 > self.currSize:
            return i * 2
        else:
            if self.heapList[i * 2] < self.heapList[i * 2 + 1]:
                return i * 2
            else:
                return i * 2 + 1

    def delMin(self):
        r = self.heapList[1]
        self.heapList[1] = self.heapList[self.currSize]
        self.currSize = self.currSize - 1
        self.heapList.pop()
        self.Down(1)
        return r

    def buildHeap(self, arr):
        k = len(arr)
        i = k // 2
        self.currSize = k
        self.heapList = [0] + arr
        while (i > 0):
            self.Down(i)
            i = i - 1
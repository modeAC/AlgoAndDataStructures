def is_float(str):
    if str.isdigit() == 1:
        return False
    else:
        try:
            float(str)
            return True
        except ValueError:
            return False

#Bubble Sort

def bubbleSort(arr):
    n = len(arr) - 1
    for i in range(n):
        for j in range(n - i):
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]

#Merge Sort - Bottom-Up Approach

def merge(arr, lo, mid, hi, curr):
    lo = min(len(arr), lo)
    mid = min(len(arr), mid)
    hi = min(len(arr), hi)
    ind_1 = lo
    ind_2 = mid
    while ind_1 < mid and ind_2 < hi:
        if arr[ind_1] < arr[ind_2]:
            curr.append(arr[ind_1])
            ind_1 += 1
        else:
            curr.append(arr[ind_2])
            ind_2 += 1
    while ind_1 < mid:
        curr.append(arr[ind_1])
        ind_1 += 1
    while ind_2 < hi:
        curr.append(arr[ind_2])
        ind_2 += 1


def mergeSort(arr):
    aux_arr = []
    width = 1
    while width < len(arr):
        for i in range(0, len(arr), 2 * width):
            lo = i
            mid = i + width
            hi = i + 2 * width
            merge(arr, lo, mid, hi, aux_arr)

        for i in range(len(aux_arr)):
            arr[i] = aux_arr[i]
        aux_arr.clear()
        width *= 2

#Quicksort modern partitioning (Lomuto partition) with Tukey's ninther pivot

def med3a(arr, b, mid, end):
    if arr[b] < arr[mid]:
        if arr[mid]< arr[end]:
            return mid
        elif arr[b] < arr[end]:
            return end
        else:
            return b
    else:
        if arr[end] < arr[mid]:
            return mid
        elif arr[end] < arr[b]:
            return end
        else:
            return b


def tukeysNinther(arr, lo, hi):
    if lo < hi:
        N = hi - lo+1
        delta = N//8
        med_1 = med3a(arr, lo, lo+delta, lo+2*delta)
        med_2 = med3a(arr, lo+2*delta, lo+3*delta, lo+4*delta)
        med_3 = med3a(arr, hi-2*delta, hi-delta, hi)
        med = med3a(arr, med_1, med_2, med_3)
        return med
    else:
        return hi

def partition(arr, lo, hi):
    pivot = arr[tukeysNinther(arr, lo, hi)]
    l=[]
    r=[]
    i=[]
    for j in range(low, high):
        if arr[j] < pivot:
            l.append(A[j])
        elif arr[j] == pivot:
            i.append(A[j])
        else:
            r.append(A[j])
    arr = l+i+r
    return len(l)

def quickSort(arr):
    if len(arr) > 1:
        pivot = arr[tukeysNinther(arr, 0, len(arr)-1)]
        l = []
        r = []
        i = []
        for j in range(len(arr)):
            if arr[j] < pivot:
                l.append(arr[j])
            elif arr[j] == pivot:
                i.append(arr[j])
            else:
                r.append(arr[j])
        quickSort(l)
        quickSort(r)
        k=0
        for x in l + i + r:
            arr[k] = x
            k+=1

#Counting Sort

def countingSort(arr):
    n = len(arr)
    aux_arr = []
    for i in range(2*max(arr)):
        aux_arr.append(0)
    for elem in arr:
        aux_arr[elem]+=1
    arr.clear()
    for k in range(len(aux_arr)):
        if aux_arr[k] != 0:
            for i in range(aux_arr[k]):
                arr.append(k)
    return arr
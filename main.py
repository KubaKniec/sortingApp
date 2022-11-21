import sys
import random
import time

sys.setrecursionlimit(1000000)


def mergeSort(arr):
    t = time.process_time()
    if len(arr) > 1:
        # dzielenie tablicy na 2 mniejsze
        mid = len(arr) // 2

        # lewa tablica
        L = arr[:mid]

        # prawa tablica
        R = arr[mid:]

        # Sortowanie lewej
        mergeSort(L)

        # Sortowanie prawej
        mergeSort(R)

        i = j = k = 0

        # Kopiowanie do tymczasowych tablic
        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Sprawdzenie czy coś zostało
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

    ms_execution_time = time.process_time() - t
    return ms_execution_time



def heapify(arr, n, i):
    biggest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[i] < arr[l]:
        biggest = l

    if r < n and arr[biggest] < arr[r]:
        biggest = r

    if biggest != i:
        arr[i], arr[biggest] = arr[biggest], arr[i]
        heapify(arr, n, biggest)

def heapSort(arr):
    t = time.process_time()
    n = len(arr)
    for i in range(n // 2, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

    ms_execution_time = time.process_time() - t
    return ms_execution_time




def quickSort(arr, l, r):
    t = time.process_time()
    if l< r:
        x = partition(arr, l, r)
        quickSort(arr, l, x - 1)
        quickSort(arr, x + 1, r)
    qs_execution_time = time.process_time() - t
    return qs_execution_time

def partition(arr, l, r):
    pivot = arr[random.randint(l, r)]
    small = l
    for x in range(l, r):
        if arr[x]<=pivot:
            arr[small], arr[x] = arr[x], arr[small]
            small+=1
    arr[small], arr[r] = arr[r], arr[small]
    return small


def printList(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()


def generateArray():
    x = []
    randomRange = random.randint(100000, 1000000)
    for i in range(randomRange):
        y = random.randrange(1, 5000)
        x.insert(i, y)
    return x



if __name__ == '__main__':
    randomArray = generateArray()
    arrayForQuickSort = arrayForHeapSort = arrayForMergeSort = randomArray

    print("Wielkosc wylosowanej tablicy: ", str(len(arrayForMergeSort)), "\n")


######## -> MERGE SORT ########
    print("### MERGE SORT ###")
    print("(sortowanie LOSOWEJ tablicy)")
    print("Posortowane w czasie: ", str(mergeSort(arrayForMergeSort)), " sekund\n")
    # printList(arrayForMergeSort)
    input("[enter], aby przejsc dalej")

    print("(sortowanie POSORTOWANEJ tablicy)")
    print("Posortowane w czasie: ", str(mergeSort(arrayForMergeSort)), " sekund\n")
    # printList(arrayForMergeSort)
    input("[enter], aby przejsc dalej")

    arrayForMergeSort.reverse()
    print("sortowanie ODWRÓCONEJ tablicy")
    print("Posortowane w czasie: ", str(mergeSort(arrayForMergeSort)), " sekund\n")
    # printList(arrayForMergeSort)
    print("____________________")
    input("[enter], aby przejsc dalej")


######## -> HEAP SORT ########

    print("### HEAP SORT ###")
    print("(sortowanie LOSOWEJ tablicy)")
    print("Posortowane w czasie: ", str(heapSort(arrayForHeapSort)), " sekund\n")
    #printList(arrayForHeapSort)
    input("[enter], aby przejsc dalej")

    print("(sortowanie POSORTOWANEJ tablicy)")
    print("Posortowane w czasie: ", str(heapSort(arrayForHeapSort)), " sekund\n")
    #printList(arrayForHeapSort)
    input("[enter], aby przejsc dalej")

    arrayForMergeSort.reverse()
    print("sortowanie ODWRÓCONEJ tablicy")
    print("Posortowane w czasie: ", str(heapSort(arrayForHeapSort)), " sekund\n")
    print("____________________")
    #printList(arrayForHeapSort)
    input("[enter], aby przejsc dalej")


######## -> QUICK SORT ########

    print("### QUICK SORT ###")
    print("(sortowanie LOSOWEJ tablicy)")
    print("Posortowane w czasie: ", str(quickSort(arrayForQuickSort,0,len(arrayForQuickSort)-1)), " sekund\n")
    # printList(arrayForQuickSort)
    input("[enter], aby przejsc dalej")

    print("(sortowanie POSORTOWANEJ tablicy)")
    print("Posortowane w czasie: ", str(quickSort(arrayForQuickSort,0,len(arrayForQuickSort)-1)), " sekund\n")
    # printList(arrayForQuickSort)
    input("[enter], aby przejsc dalej")

    arrayForMergeSort.reverse()
    print("sortowanie ODWRÓCONEJ tablicy")
    print("Posortowane w czasie: ", str(quickSort(arrayForQuickSort,0,len(arrayForQuickSort)-1)), " sekund\n")
    # printList(arrayForQuickSort)


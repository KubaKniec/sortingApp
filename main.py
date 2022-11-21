import sys
import random
import time

sys.setrecursionlimit(10000)


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

# def heapSort(arr):


def printList(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()

def generateArray():
    x = []
    randomRange = random.randint(100000, 1000000)
    for i in range(randomRange):
        y = random.randrange(1, 1000)
        x.insert(i, y)
    return x




if __name__ == '__main__':
    arrayForMergeSort = generateArray()
    print("Wielkosc wylosowanej tablicy: ", str(len(arrayForMergeSort)), "\n")
    print("(sortowanie LOSOWEJ tablicy)")
    print("Posortowane w czasie: ", str(mergeSort(arrayForMergeSort)), " sekund\n")

    print("(sortowanie POSORTOWANEJ tablicy)")
    print("Posortowane w czasie: ", str(mergeSort(arrayForMergeSort)), " sekund\n")

    arrayForMergeSort.reverse()
    print("sortowanie ODWRÓCONEJ tablicy")
    print("Posortowane w czasie: ", str(mergeSort(arrayForMergeSort)), " sekund\n")





import findSmallest


def selectionSort(arr):
    newArr = []
    for i in range(len(arr)):
        smallest = findSmallest.findSmallest(arr)
        newArr.append(arr.pop(smallest))
    return newArr


print(selectionSort([5, 1, 3, 6, 10]))

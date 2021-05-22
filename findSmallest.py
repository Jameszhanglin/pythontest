def findSmallest(arr):
    smallest = arr[0]  # --------存储最小值
    smallest_index = 0  # --------存储最小元素的索引
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

def count(list):  # 输出数组中的个数
    if list == []:
        return 0
    else:
        return 1 + count(list[1:])


print(count([2, 3, 5, 6, 1, 10]))

#找数组中的最大值
def findMax(list):
    if len(list) == 2:
        return list[0] if list[0] > list[1] else list[1]
    listmax = max(list[1:])
    return list[0] if list[0] > listmax else listmax


print(findMax([1, 2, 4, 5, 8, 10]))


# 快速排序
def quicksort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        grater = [i for i in array[1:] if i > pivot]
        return quicksort(less) + [pivot] + quicksort(grater)


print(quicksort([10, 5, 2, 3]))

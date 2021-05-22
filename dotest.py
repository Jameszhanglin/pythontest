def count(list):
    if list == []:
        return 0
    else:
        return 1 + count(list[1:])


print(count([2, 3, 5, 6, 1, 10]))


def findMax(list):
    if len(list) == 2:
        return list[0] if list[0] > list[1] else list[1]
    listmax = max(list[1:])
    return list[0] if list[0] > listmax else listmax


print(findMax([1, 2, 4, 5, 8, 10]))

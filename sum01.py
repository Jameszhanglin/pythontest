

def binary_search(list,item):   # 传入数组 和目标数
    low = 0                     #low 和 high 要用于跟踪查找部分
    high =len(list)-1
    while low<=high:            #只要范围没有缩小到只包含一个元素，
        mid = (low + high) / 2  # 只检查中间元素
        guess = list[mid]
        if guess == item:       #找到元素
           return mid
        if guess > item:        #如果大于
           high = mid - 1
        else:
            low = mid + 1       #如果小于
     return  None
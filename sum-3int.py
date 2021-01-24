def sumThree(arrNums):
    
    result = []
    arrNums.sort()
    length = len(arrNums)

    for i in range(length-2):
        if i>0 and arrNums[i] == arrNums[i-1]:
            continue
        left = i + 1
        right = length - 1
       
        while left < right:
            sum = arrNums[i] + arrNums[left] + arrNums[right]
            if sum<0:
                # as array is sorted
                left = left + 1
            elif sum>0:
                right = right + 1
            else:
                result.append(arrNums[i], arrNums[left], arrNums[right])
                while left < right and arrNums[left] == arrNums[right]:
                    left = left+1
                while left < right and arrNums[right] == arrNums[right-1]:
                    right = right - 1
                left += 1
                right += 1
    
    return result

print(sumThree ([1,2,-5,-3,4,5,6,-2,-3]))
    